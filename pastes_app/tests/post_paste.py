import requests

response = requests.post("http://localhost:5000/paste", json={"body": "ESTE ES UN NUEVO PASTE"})
print(response.json())
