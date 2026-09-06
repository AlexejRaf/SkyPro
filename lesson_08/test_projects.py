import requests
from conftest import API_BASE_URL


class TestProjectsAPI:

    # Позитивные тесты:
    def test_create_project_positive(self, api_headers):
        payload = {"title": "Позитивный проект"}
        response = requests.post(
            f"{API_BASE_URL}/projects",
            json=payload,
            headers=api_headers
        )

        assert response.status_code == 201, (
            f"Ожидался 201, получен {response.status_code}"
        )
        data = response.json()
        assert "id" in data, "Ответ не содержит id проекта"

        project_id = data["id"]
        get_response = requests.get(
            f"{API_BASE_URL}/projects/{project_id}",
            headers=api_headers
        )
        assert get_response.status_code == 200, (
            "Не удалось получить созданный проект"
        )
        assert get_response.json()["title"] == payload["title"], (
            "Название проекта не совпадает"
        )

    def test_create_project_with_users(self, api_headers):
        user_id = "80eed1bd-eda3-4991-ac17-09d28566749d"
        payload = {
            "title": "Проект с пользователем",
            "users": {user_id: "admin"}
        }
        response = requests.post(
            f"{API_BASE_URL}/projects",
            json=payload,
            headers=api_headers
        )
        assert response.status_code in (201, 400), (
            f"Ожидался 201 или 400, получен {response.status_code}"
        )
        if response.status_code == 201:
            assert response.json()["title"] == payload["title"]

    def test_get_project_positive(self, api_headers, created_project_id):
        response = requests.get(
            f"{API_BASE_URL}/projects/{created_project_id}",
            headers=api_headers
        )
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}"
        )
        data = response.json()
        assert data["id"] == created_project_id, "ID проекта не совпадает"
        assert "title" in data, "В ответе нет поля title"

    def test_update_project_positive(self, api_headers, created_project_id):
        new_title = "Обновлённый проект"
        payload = {"title": new_title}
        response = requests.put(
            f"{API_BASE_URL}/projects/{created_project_id}",
            json=payload,
            headers=api_headers
        )
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}"
        )

        get_response = requests.get(
            f"{API_BASE_URL}/projects/{created_project_id}",
            headers=api_headers
        )
        assert get_response.status_code == 200, (
            "Не удалось получить проект после обновления"
        )
        assert get_response.json()["title"] == new_title, (
            "Название не обновилось"
        )

    # Негативные тесты:

    def test_create_project_missing_title(self, api_headers):
        payload = {}
        response = requests.post(
            f"{API_BASE_URL}/projects",
            json=payload,
            headers=api_headers
        )
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )
        assert "error" in response.json(), "Нет сообщения об ошибке"

    def test_create_project_empty_title(self, api_headers):
        payload = {"title": ""}
        response = requests.post(
            f"{API_BASE_URL}/projects",
            json=payload,
            headers=api_headers
        )
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )

    def test_get_project_invalid_id(self, api_headers):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = requests.get(
            f"{API_BASE_URL}/projects/{fake_id}",
            headers=api_headers
        )
        assert response.status_code == 404, (
            f"Ожидался 400, получен {response.status_code}"
        )

    def test_update_project_invalid_id(self, api_headers):
        fake_id = "00000000-0000-0000-0000-000000000000"
        payload = {"title": "Неважно"}
        response = requests.put(
            f"{API_BASE_URL}/projects/{fake_id}",
            json=payload,
            headers=api_headers
        )
        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}"
        )

    def test_update_project_empty_title(self, api_headers, created_project_id):
        payload = {"title": ""}
        response = requests.put(
            f"{API_BASE_URL}/projects/{created_project_id}",
            json=payload,
            headers=api_headers
        )
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )
