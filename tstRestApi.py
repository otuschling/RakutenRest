import requests
response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.headers["date"])

