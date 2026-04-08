import os
import requests

headers = {
    "X-SM-API-TOKEN": os.environ["SEPPMAIL_API_TOKEN"],
    "X-SM-API-SECRET": os.environ["SEPPMAIL_API_SECRET"],
}
response = requests.get("https://mail.example.com:8445/v1/version", headers=headers, timeout=15)
print(response.status_code)
print(response.text)
