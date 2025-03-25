import asyncio

import pendulum
from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


async def main():
    start = pendulum.now()

    topic_1 = Topic(id=1)
    topic_2 = Topic(id=2)

    pub_1 = Publisher(id=1)
    pub_2 = Publisher(id=2)

    sub_1 = Subscriber(id=1)
    sub_2 = Subscriber(id=2)
    sub_3 = Subscriber(id=3)

    queues = []
    q1 = await sub_1.subscribe(topic=topic_1)
    q2 = await sub_2.subscribe(topic=topic_2)
    q3 = await sub_3.subscribe(topic=topic_1)
    q4 = await sub_3.subscribe(topic=topic_2)
    queues.extend([q1, q2, q3, q4])

    for i in range(
        20000
    ):  # No max number here, whereas threads are limited to roughly 2000
        sub = Subscriber(id=i + 4)
        q = await sub.subscribe(topic=topic_1)
        queues.append(q)

    await pub_1.publish(topic=topic_1, item="Pub 1 to topic 1")
    await pub_2.publish(topic=topic_1, item="Pub 2 to topic 1")

    await pub_1.publish(topic=topic_2, item="Pub 1 to topic 2")
    await pub_2.publish(topic=topic_2, item="Pub 2 to topic 2")

    for i in range(50):
        pub = Publisher(id=3)
        await pub.publish(topic=topic_1, item=f"Pub message {i} to topic 1")

    for q in queues:
        await q.join()

    print((pendulum.now() - start).seconds)


if __name__ == "__main__":
    asyncio.run(main())
