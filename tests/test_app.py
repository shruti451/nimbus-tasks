from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app.app as app_module


def test_home_page():
    app_module.redis_client = MagicMock()
    app_module.redis_client.get.return_value = None

    app_module.db = MagicMock()
    app_module.db.cursor.return_value.fetchall.return_value = []

    client = app_module.app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_create_task():
    app_module.redis_client = MagicMock()
    app_module.db = MagicMock()

    client = app_module.app.test_client()

    response = client.post(
        "/",
        data={"quest": "Learn Docker"}
    )

    assert response.status_code == 302
    app_module.db.commit.assert_called_once()
    app_module.redis_client.delete.assert_called_once_with("tasks")