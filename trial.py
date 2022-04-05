import requests

response = requests.get("https://api.npoint.io/ab312a499fe456df41c6").json()
print(response)