from kafka import KafkaProducer
import json
import time
producer=KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")


)
for i in range(10):
    message={
        "name":f"ashrit{i+1}",
        "age":20+i
    }
    producer.send(
        "ashrit",
        value=message
    )
    print("Sent:",message)
    time.sleep(1)