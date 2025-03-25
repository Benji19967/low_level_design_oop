import pendulum
from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


def main() -> None:

    start = pendulum.now()

    topic_1 = Topic[str](id=1)
    topic_2 = Topic[str](id=2)

    pub_1 = Publisher(id=1)
    pub_2 = Publisher(id=2)

    sub_1 = Subscriber[str](id=1)
    sub_2 = Subscriber[str](id=2)
    sub_3 = Subscriber[str](id=3)

    queues = []
    q1 = sub_1.subscribe(topic=topic_1)
    q2 = sub_2.subscribe(topic=topic_2)
    q3 = sub_3.subscribe(topic=topic_1)
    q4 = sub_3.subscribe(topic=topic_2)
    queues.extend([q1, q2, q3, q4])

    for i in range(2000):  # there is a max number (of threads) here (roughly 2000)
        sub = Subscriber[str](id=i + 4)
        q = sub.subscribe(topic=topic_1)
        queues.append(q)

    pub_1.publish(topic=topic_1, item="Pub 1 to topic 1")
    pub_2.publish(topic=topic_1, item="Pub 2 to topic 1")

    pub_1.publish(topic=topic_2, item="Pub 1 to topic 2")
    pub_2.publish(topic=topic_2, item="Pub 2 to topic 2")

    for i in range(50):
        pub = Publisher(id=3)
        pub.publish(topic=topic_1, item=f"Pub message {i} to topic 1")

    for q in queues:
        q.join()

    print((pendulum.now() - start).seconds)


if __name__ == "__main__":
    main()
