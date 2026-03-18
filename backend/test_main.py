import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "FinSense AI Backend is running"

def test_create_category():
    resp = client.post("/categories", json={"name": "TestCat"})
    assert resp.status_code in (200, 409)
    if resp.status_code == 200:
        assert resp.json()["name"] == "TestCat"
    elif resp.status_code == 409:
        assert resp.json()["detail"] == "Category already exists"

def test_get_categories():
    resp = client.get("/categories")
    assert resp.status_code == 200
    assert any(cat["name"] == "TestCat" for cat in resp.json())

def test_create_transaction():
    categories = client.get("/categories").json()
    cat_id = categories[0]["id"]
    resp = client.post("/transactions", json={"amount": 10.5, "description": "TestTx", "category_id": cat_id})
    assert resp.status_code == 200
    assert resp.json()["amount"] == 10.5
    assert resp.json()["description"] == "TestTx"

def test_get_transactions():
    resp = client.get("/transactions")
    assert resp.status_code == 200
    assert any(tx["description"] == "TestTx" for tx in resp.json())

def test_analytics():
    resp = client.get("/analytics")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_trends():
    resp = client.get("/trends")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_forecast():
    resp = client.get("/forecast")
    assert resp.status_code == 200
    assert "estimated_balance" in resp.json()
    assert "recurring_expenses" in resp.json()
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "FinSense AI Backend" in response.json()["message"]

def test_create_category():
    response = client.post("/categories", json={"name": "TestCat"})
    assert response.status_code in (200, 409)
    if response.status_code == 200:
        assert response.json()["name"] == "TestCat"
    elif response.status_code == 409:
        assert response.json()["detail"] == "Category already exists"

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_transaction():
    # Get category id
    categories = client.get("/categories").json()
    cat_id = categories[0]["id"] if categories else None
    response = client.post("/transactions", json={"amount": 10.5, "description": "uber ride", "category_id": cat_id})
    assert response.status_code == 200
    assert response.json()["amount"] == 10.5

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_analytics():
    response = client.get("/analytics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_trends():
    response = client.get("/trends")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_forecast():
    response = client.get("/forecast")
    assert response.status_code == 200
    assert "estimated_balance" in response.json()
