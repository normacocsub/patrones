import requests
from circuitbreaker import circuit



@circuit(failure_threshold=3, expected_exception=Exception)
def external_api_call(url, data):
    response = requests.post(url, json=data.dict())
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to retrieve data from external API")

def fallback():
    return {"fallback_value": "default"}

def make_request(url, data):
    try:
        data = external_api_call(url)
        return data
    except:
        return fallback()