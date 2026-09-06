import os
import pytest
import requests

API_BASE_URL = "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_token():
    """Получает токен из переменной окружения YOUGILE_API_KEY."""
    token = os.getenv("YOUGILE_API_KEY")
    if not token:
        pytest.fail("Переменная окружения YOUGILE_API_KEY не установлена!")
    return token


@pytest.fixture(scope="session")
def api_headers(api_token):
    """Возвращает заголовки для запросов к API."""
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }


@pytest.fixture
def created_project_id(api_headers):
    """
    Создаёт временный проект для тестов и возвращает его ID.
    После завершения теста проект удаляется.
    """
    payload = {
        "title": "Автотест-проект"
    }
    response = requests.post(
        f"{API_BASE_URL}/projects",
        json=payload,
        headers=api_headers
    )
    assert response.status_code == 201, f"Не удалось создать проект: {
        response.text}"
    project_id = response.json()["id"]

    yield project_id

    delete_response = requests.delete(
        f"{API_BASE_URL}/projects/{project_id}",
        headers=api_headers
    )
    if delete_response.status_code not in (200, 204, 404):
        print(f"Не удалось удалить проект {
            project_id}: {delete_response.text}")
