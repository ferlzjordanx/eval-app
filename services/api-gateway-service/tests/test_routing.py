from fastapi.testclient import TestClient

from main import app, find_service_for_path, get_service_url


def test_health_endpoint():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_find_service_for_known_paths():
    assert find_service_for_path("/v1/api/auth/login") == "user-service"
    assert find_service_for_path("v1/api/tests") == "test-management-service"
    assert find_service_for_path("/v1/api/questions") == "question-management-service"


def test_get_service_url_uses_compose_dns():
    assert get_service_url("user-service") == "http://user-service:8002"
