import pytest
from fastapi.testclient import TestClient

from api.src.create_app import create_app
from sqlalchemy.orm import Session

@pytest.fixture
def api_client() -> TestClient:
    api = create_app()
    client = TestClient(api)

    return client


@pytest.fixture
def db_session() -> Session: # type: ignore
    from adapters.src.repositories import Connection, SessionManager, SQLConnection

    connection: Connection = SQLConnection()
    SessionManager.initialize_session(connection)
    yield SessionManager.get_session()
    SessionManager.close_session()
