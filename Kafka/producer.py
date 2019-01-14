from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('sample', b'hello world!')
producer.send('sample', key=b'message2', value=b'this is the kafka')
producer.flush()