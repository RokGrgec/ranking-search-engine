from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_search_word():
    data = "test"
    response = client.post(f"/search/?word={data}")
    assert response.status_code == 200


def test_add_document():
    data = "Test text."
    response = client.post("/add_document", json={"text": data})
    assert response.status_code == 200
