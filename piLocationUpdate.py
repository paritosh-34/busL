import requests
import json
import time

my_url = "http://127.0.0.1:5000/post?lat=1.2.3.4&lon=1.2.3.4"
# Change the url respectively

while True:
    # This is the format to send lat lon
    data = {
        "lat": "1.1.1.1",  # lat here
        "lon": "2.2.2.2",  # lon here
    }
    y = json.dumps(data)
    r = requests.post(url=my_url)
    print(r)
    # time.sleep(6)
    break
