import asyncio
from typing import Generic, TypeVar

from topic import Topic

T = TypeVar("T")


class Subscriber(Generic[T]):
    def __init__(self, id: int) -> None:
        self._id = id
        self._subscriptions: dict[int, asyncio.Queue[T]] = {}

    async def subscribe(self, topic: Topic[T]) -> asyncio.Queue[T]:
        q = topic.subscribe(subscriber_id=self._id)
        self._subscriptions[topic.id] = q
        asyncio.create_task(self._worker(q))
        return q

    async def _worker(self, q: asyncio.Queue[T]) -> None:
        while True:
            item = await q.get()
            if item is None:
                q.task_done()
                print("DONE")
                return
            asyncio.create_task(self._do_task(item))
            q.task_done()

    async def _do_task(self, item: T) -> None:
        print(f"Subscriber {self._id}: working on {item}")
        await asyncio.sleep(0.1)
