import json
import requests
import time
import json
from kafka import KafkaProducer
url="https://www.alphavantage.co/query"
# header={
#     "key":"8ED74RHAZWLVRS1O"
# }

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "8ED74RHAZWLVRS1O"
}
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
while True:
    respond=requests.get(url,params=params)

    if respond.status_code==200:
        print("request is 200")
        # print(respond.json())
        print("json is dn")
    else:
        print("error")

    print("Waiting 5 seconds...")
    time.sleep(5)