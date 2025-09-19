# from app import app

# def test_home():
#     client = app.test_client()
#     response = client.get("/")
#     assert response.data == b"Hello, CI/CD!"
#     assert response.status_code == 200
#     print("1")
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    print("Response data:", response.data)        # <-- prints actual response
    print("Status code:", response.status_code)  # <-- prints HTTP status
    assert response.data == b"Hello, CI/CD!"
    assert response.status_code == 200

