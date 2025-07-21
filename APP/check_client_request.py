import requests
from pprint import pprint

url = "http://127.0.0.1:8000/predict/df_phishing"

params = {
    "UsingIP": 1,
    "LongURL": 0,
    "ShortURL": -1
}


res = requests.get(url, params=params)

print("GET response:")
print(res)
print(res.status_code)
pprint(res.json())
