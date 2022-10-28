import sys

from nile_consumer import NileConsumer
from passthru_producer import PassthruProducer


if __name__ == '__main__':
    command_line_args = sys.argv[1:]
    servers = command_line_args[0]
    group_id = command_line_args[1]
    in_topic = command_line_args[2]
    good_topic = command_line_args[3]

    consumer = NileConsumer(servers, group_id, in_topic)
    producer = PassthruProducer(servers, good_topic)

    consumer.run(producer)
