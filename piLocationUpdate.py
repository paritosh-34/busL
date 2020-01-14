import requests
import json
import time

my_url = "http://127.0.0.1:5000/api/latlon"

while True:
    data = {
        "lat": "1.1.1.1",
        "lon": "2.2.2.2"
    }
    y = json.dumps(data)
    r = requests.post(url=my_url, json=data)
    # time.sleep(6)
    break
