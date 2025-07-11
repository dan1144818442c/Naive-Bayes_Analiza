import requests
from pprint import pprint


url = "http://127.0.0.1:8000/predict"  # הנתיב הנכון של ה-API שלך

params = {
    "UsingIP": 1,
    "LongURL": -1,
    "ShortURL": -1,
    "HTTPS": 1
  }

res = requests.get("http://127.0.0.1:8000/predict", params=params)


print("POST response:")
print(res)
print(res.status_code)
pprint(res.json())
