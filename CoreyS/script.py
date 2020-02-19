import requests

r = requests.get("https://insikten.lm.se/")
print(r.status_code)
print(r.ok)
