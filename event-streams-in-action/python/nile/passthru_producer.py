from confluent_kafka import Producer

class PassthruProducer:
    def __init__(self, servers, topic):
        config = self.create_config(servers)
        self.producer = Producer(config)
        self.topic = topic

    def process(self, message):
        self.write(self.topic, message)

    def write(self, topic, message):
        self.producer.produce(topic, value=message)

    def create_config(self, servers):
        return {
            'bootstrap.servers': servers
        }
