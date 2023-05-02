import requests
from requests.exceptions import Timeout
import time



async def post_data_with_retry(url,data, retries=3, backoff_factor=0.5):
    for i in range(retries):
        try:
            response = requests.post(url,json=data.dict(), timeout=5)
            print("hello", response.content)
            return response.content
        except:
            if i == retries - 1:
                raise
            else:
                print(f"Timeout, retrying in {backoff_factor * (i + 1)} seconds...")
                time.sleep(backoff_factor * (i + 1))