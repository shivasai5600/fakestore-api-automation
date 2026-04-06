import requests
from config.config import BASE_URL

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get(endpoint):
    return requests.get(BASE_URL + endpoint, headers=headers)

def post(endpoint, payload):
    return requests.post(BASE_URL + endpoint, json=payload, headers=headers)

def get(endpoint):
    for _ in range(3):
        response = requests.get(BASE_URL + endpoint, headers=headers)
        if response.status_code != 403:
            return response
    return response