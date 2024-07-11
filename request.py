import requests

url = "http://127.0.0.1:8000/query"
payload = {
    "url": "https://sdmcet.ac.in/",
    "query": "principal"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
