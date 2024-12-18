from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_csv():
    data = {
        "selected_columns": ["name", "age"],
        "new_columns": {
            "country": ["USA", "Canada"],
            "status": ["active", "inactive"]
        }
    }

    response = client.post("/generate_csv/", json=data)
    
    assert response.status_code == 200
    assert "text/csv" in response.headers["Content-Type"]
