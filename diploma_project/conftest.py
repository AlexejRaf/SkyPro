"""Общие фикстуры для тестов."""
import os
from pathlib import Path
from typing import Generator

import pytest
import requests
from dotenv import load_dotenv

# Загружаем .env из папки проекта (а не из текущей директории)
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

@pytest.fixture(scope="session")
def base_url() -> str:
    """Возвращает базовый URL API.

    Returns:
        str: базовый URL из .env.
    """
    url = os.getenv("BASE_URL")
    if not url:
        pytest.fail("BASE_URL не задан в .env")
    return url

@pytest.fixture(scope="session")
def api_token() -> str:
    """Возвращает API-токен.

    Returns:
        str: API-токен из .env.
    """
    token = os.getenv("API_TOKEN")
    if not token:
        pytest.fail("API_TOKEN не задан в .env")
    return token

@pytest.fixture(scope="session")
def api_headers(api_token: str) -> dict:
    """Возвращает заголовки для API-запросов.

    Args:
        api_token: API-токен.

    Returns:
        dict: словарь с заголовками.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

@pytest.fixture(scope="session")
def api_session() -> Generator[requests.Session, None, None]:
    """Создаёт сессию requests для API-запросов.

    Yields:
        requests.Session: сессия для HTTP-запросов.
    """
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="session")
def column_id() -> str:
    """Возвращает ID колонки для создания задач.

    Returns:
        str: ID колонки из .env.
    """
    return os.getenv("COLUMN_ID", "")

@pytest.fixture(scope="session")
def assignee_id() -> str:
    """Возвращает ID исполнителя для назначения.

    Returns:
        str: ID исполнителя из .env.
    """
    return os.getenv("ASSIGNEE_ID", "")