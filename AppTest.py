from fastapi.testclient import TestClient
from main import app 
import pytest

client = TestClient(app)

def test_swagger_ui():
    """Проверява дали документацията е достъпна - критично за всеки API проект"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_redoc():
    # Check if ReDoc documentation is available
    response = client.get("/redoc")
    assert response.status_code == 200

def test_unauthorized_access():
    # Check unauthorized access to a protected endpoint
    response = client.get("/items") 
    assert response.status_code != 200