import requests
def test_frontend_backend_integration():
    frontend_url = "http://localhost:8080"
    backend_url = "http://localhost:8081"
  response = requests.get(f"{frontend_url}/greeting")
    assert response.status_code == 200
    assert "Hello from backend!" in response.text
response = requests.get(f"{backend_url}/greeting")
    assert response.status_code == 200
    assert "Hello from backend!" in response.text