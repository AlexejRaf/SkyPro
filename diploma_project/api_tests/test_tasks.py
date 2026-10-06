"""API-тесты для задач YouGile."""
from typing import Generator

import allure
import pytest

from utils.api_client import ApiClient


@pytest.fixture
def api(base_url: str, api_headers: dict) -> Generator[ApiClient, None, None]:
    """Создаёт клиент API для тестов."""
    client = ApiClient(base_url, api_headers)
    yield client
    client.close()


@allure.feature("YouGile API: Задачи")
@allure.title("Создание задачи с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_create_task(api: ApiClient, column_id: str) -> None:
    """Позитивный: создание задачи."""
    with allure.step("POST /tasks"):
        response = api.create_task("Тестовая задача", column_id)
    with allure.step("Статус 201 и есть id"):
        assert response.status_code == 201
        assert "id" in response.json()


@allure.feature("YouGile API: Задачи")
@allure.title("Получение задачи по ID")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_get_task(api: ApiClient, column_id: str) -> None:
    """Позитивный: получение задачи по ID."""
    with allure.step("Создать задачу"):
        task_id = api.create_task("Задача", column_id).json()["id"]
    with allure.step("GET /tasks/{id}"):
        response = api.get_task(task_id)
    with allure.step("Статус 200 и ID совпадает"):
        assert response.status_code == 200
        assert response.json()["id"] == task_id


@allure.feature("YouGile API: Задачи")
@allure.title("Обновление названия задачи")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_update_task(api: ApiClient, column_id: str) -> None:
    """Позитивный: обновление названия."""
    with allure.step("Создать задачу"):
        task_id = api.create_task("Старое", column_id).json()["id"]
    with allure.step("PUT /tasks/{id}"):
        new_title = "Новое название"
        response = api.update_task(task_id, {"title": new_title})
    with allure.step("Статус 200 и название обновилось"):
        assert response.status_code == 200
        assert api.get_task(task_id).json()["title"] == new_title


@allure.feature("YouGile API: Задачи")
@allure.title("Создание задачи без авторизации (негативный)")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_create_task_unauthorized(
    api: ApiClient, column_id: str
) -> None:
    """Негативный: без заголовка Authorization."""
    with allure.step("POST /tasks без Authorization"):
        response = api.create_task_without_auth(
            "Без авторизации", column_id
        )
    with allure.step("Статус 401"):
        assert response.status_code == 401


@allure.feature("YouGile API: Задачи")
@allure.title("Создание задачи без title (негативный)")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_create_task_without_title(api: ApiClient, column_id: str) -> None:
    """Негативный: без обязательного поля title."""
    with allure.step("POST /tasks без title"):
        response = api.session.post(
            f"{api.base_url}/tasks",
            json={"columnId": column_id},
        )
    with allure.step("Статус 400"):
        assert response.status_code == 400
