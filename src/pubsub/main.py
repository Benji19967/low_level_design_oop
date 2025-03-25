from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


def main():

    topic_1 = Topic()
    topic_2 = Topic()

    pub_1 = Publisher(id=1)
    pub_2 = Publisher(id=2)

    sub_1 = Subscriber(id=1)
    sub_2 = Subscriber(id=2)
    sub_3 = Subscriber(id=3)

    queues = []
    q1 = sub_1.subscribe(topic=topic_1)
    q2 = sub_2.subscribe(topic=topic_2)
    q3 = sub_3.subscribe(topic=topic_1)
    q4 = sub_3.subscribe(topic=topic_2)
    queues.extend([q1, q2, q3, q4])

    pub_1.publish(topic=topic_1, item="Pub 1 to topic 1")
    pub_2.publish(topic=topic_1, item="Pub 2 to topic 1")

    pub_1.publish(topic=topic_2, item="Pub 1 to topic 2")
    pub_2.publish(topic=topic_2, item="Pub 2 to topic 2")

    for q in queues:
        q.join()


if __name__ == "__main__":
    main()
