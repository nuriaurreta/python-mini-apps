import requests

response = requests.get("http://localhost:5000/paste/3")
print(response.json())
