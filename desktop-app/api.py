import requests

BASE_URL = "http://127.0.0.1:8000/api"
TOKEN = None  # global token storage


def login(username, password):
    global TOKEN
    response = requests.post(
        f"{BASE_URL}/login/",
        json={"username": username, "password": password}
    )
    response.raise_for_status()
    TOKEN = response.json()["token"]
    return TOKEN


def auth_headers():
    if not TOKEN:
        raise Exception("Not authenticated")
    return {
        "Authorization": f"Token {TOKEN}"
    }


def get_latest_summary():
    response = requests.get(
        f"{BASE_URL}/summary/latest/",
        headers=auth_headers()
    )
    response.raise_for_status()
    return response.json()
