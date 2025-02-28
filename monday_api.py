import requests
from config import MONDAY_API_KEY, MONDAY_BASE_URL

def get_boards():
    headers = {
        "Authorization": MONDAY_API_KEY
    }
    query = "{ boards { id name } }"
    response = requests.post(MONDAY_BASE_URL, json={'query': query}, headers=headers)
    return response.json()
