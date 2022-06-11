import requests
import json
import math


from kafka import KafkaProducer


KAFKA_URL= requests.get("http://10.0.12.82:8008/service_discovery/kafka/").text

with open('example2.txt') as json_file:
    data = json.load(json_file)
KafkaProducer(bootstrap_servers=[KAFKA_URL]).send('esight_interface', json.dumps(data).encode('ascii'))