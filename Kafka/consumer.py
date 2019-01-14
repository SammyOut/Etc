from kafka import KafkaConsumer

consumer = KafkaConsumer('sample')
for message in consumer:
    print(message)
