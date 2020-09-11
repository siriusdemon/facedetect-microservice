import requests

url = "http://localhost:5000/"

img = {"image": ('my.png', open("my.png", 'rb'), 'image/png')}

resp = requests.post(url, files=img)

print(resp)
print(resp.json())