# Example unit tests
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API!"}


def test_predict_success(client):
    """
    Test case of correct prediction
    """
    input_data = {
        "age": 37,
        "workclass": "Private",
        "fnlwgt": 280464,
        "education": "Some-college",
        "education-num": 10,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 80,
        "native-country": "United-States",
    }
    response = client.post("/predict/", json=input_data)
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_predict_invalid_input(client):
    """
    Test case where the data has an error
    """
    input_data = {
        "age": "Young",  # wrong data type
        "workclass": "Private",
        "fnlwgt": 280464,
        "education": "Some-college",
        "education-num": 10,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 80,
        "native-country": "United-States",
    }
    response = client.post("/predict/", json=input_data)
    assert response.status_code == 422  # Unprocessable Entity
