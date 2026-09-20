from kafka import KafkaConsumer
import json


consumer=KafkaConsumer(
    "ashrit",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

for message in consumer:
    data =message.value
    print(data["name"],data["age"])