"""Клиент для работы с API YouGile."""
from typing import Any, Optional

import requests


class ApiClient:
    """Клиент для API-запросов к YouGile."""

    def __init__(self, base_url: str, headers: dict) -> None:
        """Инициализирует клиент.

        Args:
            base_url: базовый URL API.
            headers: заголовки для запросов (Authorization, Content-Type).
        """
        self.base_url = base_url
        self.headers = headers
        self.session = requests.Session()
        self.session.headers.update(headers)

    def create_task(
        self,
        title: str,
        column_id: str,
        assignee_id: Optional[str] = None,
    ) -> requests.Response:
        """Создаёт задачу.

        Args:
            title: название задачи.
            column_id: ID колонки, куда добавить задачу.
            assignee_id: ID исполнителя (опционально).

        Returns:
            requests.Response: ответ сервера.
        """
        payload: dict[str, Any] = {
            "title": title,
            "columnId": column_id,
        }
        if assignee_id:
            payload["assigned"] = [assignee_id]

        return self.session.post(
            f"{self.base_url}/tasks",
            json=payload,
        )

    def get_task(self, task_id: str) -> requests.Response:
        """Получает задачу по ID.

        Args:
            task_id: ID задачи.

        Returns:
            requests.Response: ответ сервера.
        """
        return self.session.get(
            f"{self.base_url}/tasks/{task_id}",
        )

    def update_task(
        self,
        task_id: str,
        payload: dict[str, Any],
    ) -> requests.Response:
        """Обновляет задачу.

        Args:
            task_id: ID задачи.
            payload: поля для обновления.

        Returns:
            requests.Response: ответ сервера.
        """
        return self.session.put(
            f"{self.base_url}/tasks/{task_id}",
            json=payload,
        )

    def create_task_without_auth(
        self,
        title: str,
        column_id: str,
    ) -> requests.Response:
        """Создаёт задачу без заголовка Authorization.

        Args:
            title: название задачи.
            column_id: ID колонки.

        Returns:
            requests.Response: ответ сервера.
        """
        return requests.post(
            f"{self.base_url}/tasks",
            json={"title": title, "columnId": column_id},
            headers={"Content-Type": "application/json"},
        )

    def close(self) -> None:
        """Закрывает сессию."""
        self.session.close()
