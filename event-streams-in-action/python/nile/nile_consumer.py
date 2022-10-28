from confluent_kafka import Consumer


class NileConsumer:
    def __init__(self, servers, group_id, topic):
        config = self.create_config(servers, group_id)
        self.consumer = Consumer(config)
        self.topic = topic

    def run(self, producer):
        self.consumer.subscribe([self.topic])
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None: continue
                producer.process(msg.value())
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()

    def create_config(self, servers, group_id):
        return {
            'bootstrap.servers': servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }
