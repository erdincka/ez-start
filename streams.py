import logging
import sys

import common

logger = logging.getLogger(__name__)


def produce(stream: str, topic: str, message: str):
    from confluent_kafka import Producer

    logger.debug("Stream path: %s", stream)
    p = Producer({"streams.producer.default.stream": stream})

    try:
        logger.info("sending message: %s", message)
        p.produce(topic, message.encode("utf-8"))

    except Exception as error:
        logger.warning(error)
        return False

    finally:
        p.flush()

    return True


def consume(stream: str, topic: str, consumer_group: str):
    from confluent_kafka import Consumer, KafkaError

    logger.info("Stream: %s Topic: %s", stream, topic)

    consumer = Consumer(
        {"group.id": consumer_group, "default.topic.config": {"auto.offset.reset": "earliest"}}
    )

    try:

        consumer.subscribe([f"{stream}:{topic}"])

        while True:
            message = consumer.poll(timeout=5.0)

            if message is None: raise EOFError

            if not message.error(): yield message.value().decode("utf-8")

            elif message.error().code() == KafkaError._PARTITION_EOF:
                logger.info("No more messages in topic: %s", topic)
                raise EOFError
            # silently ignore other errors
            else: logger.warning(message.error())

    except Exception as error:
        logger.warning(error)

    finally:
        consumer.close()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        if sys.argv[1] == "produce":
            with open("./data/Testing_set_ccpp.csv", "r") as f:
                for i, line in enumerate(f):
                    if i > 10: break
                    print(produce("/apps/stream1", "topic1", line))

        elif sys.argv[1] == "consume":
            for msg in consume("/apps/stream1", "topic1", "cg1"):
                print(msg)

        else:
            logger.error("Don't know how to do anything beyond produce|consume")

    else:
        print(f'Usage: python3 {sys.argv[0]} produce|consume')