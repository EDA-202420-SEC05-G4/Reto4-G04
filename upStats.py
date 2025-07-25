import requests
import json

post_url = "http://34.31.27.183:8000/data"

with open("report.json", "r") as f:
    payload = json.load(f)

response = requests.post(post_url, json=payload)
print(response.json())
