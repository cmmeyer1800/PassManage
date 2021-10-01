import requests

data = {"message": "Hello world!"}

resp = requests.get('http://127.0.0.1:8000/dec', json={"message": requests.get('http://127.0.0.1:8000/enc', json=data).text}).text
print(resp)