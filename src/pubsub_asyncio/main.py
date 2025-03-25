import asyncio

import pendulum
from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


async def main() -> None:

    topic_1 = Topic[str](id=1)
    topic_2 = Topic[str](id=2)

    pub_1 = Publisher[str](id=1)
    pub_2 = Publisher[str](id=2)

    sub_1 = Subscriber[str](id=1)
    sub_2 = Subscriber[str](id=2)
    sub_3 = Subscriber[str](id=3)

    queues = []
    q1 = await sub_1.subscribe(topic=topic_1)
    q2 = await sub_2.subscribe(topic=topic_2)
    q3 = await sub_3.subscribe(topic=topic_1)
    q4 = await sub_3.subscribe(topic=topic_2)
    queues.extend([q1, q2, q3, q4])

    for i in range(
        1000
    ):  # No max number here, whereas threads are limited to roughly 2000
        sub = Subscriber[str](id=i + 4)
        q = await sub.subscribe(topic=topic_1)
        queues.append(q)

    await pub_1.publish(topic=topic_1, item="Pub 1 to topic 1")
    await pub_2.publish(topic=topic_1, item="Pub 2 to topic 1")

    await pub_1.publish(topic=topic_2, item="Pub 1 to topic 2")
    await pub_2.publish(topic=topic_2, item="Pub 2 to topic 2")

    for i in range(100):
        pub = Publisher[str](id=3)
        await pub.publish(topic=topic_1, item=f"Pub message {i} to topic 1")

    for q in queues:
        await q.join()

    # Optionally, end the listener tasks
    await pub.publish(topic=topic_1, item=None)  # type: ignore


if __name__ == "__main__":
    start = pendulum.now()
    asyncio.run(main())
    print((pendulum.now() - start).seconds)
