"""Offline intake tests; no live LLM or external credentials are needed."""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_intake_returns_receipt():
    payload = {"tenant_id":"demo","question":"Compare the findings","documents":[{"title":"Report A","text":"One finding."}]}
    response = client.post("/research", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["document_count"] == 1
    assert data["total_characters"] == len("One finding.")
    assert data["tenant_id"] == "demo"
    assert data["status"] == "received"

def test_blank_document_is_rejected():
    payload = {"tenant_id":"demo","question":"Compare the findings","documents":[{"title":"Report A","text":"  "}]}
    assert client.post("/research", json=payload).status_code == 422

def test_too_many_documents_are_rejected():
    payload = {"tenant_id":"demo","question":"Compare the findings","documents":[{"title":"R","text":"x"}] * 6}
    assert client.post("/research", json=payload).status_code == 422

def test_invalid_tenant_identifier_is_rejected():
    payload = {"tenant_id":"../../admin","question":"Compare the findings","documents":[{"title":"R","text":"x"}]}
    assert client.post("/research", json=payload).status_code == 422
