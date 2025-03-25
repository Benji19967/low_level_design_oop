import asyncio
from typing import Generic, TypeVar

T = TypeVar("T")


class Topic(Generic[T]):
    def __init__(self, id: int) -> None:
        self._id = id
        self._subscriptions: dict[int, asyncio.Queue[T]] = {}

    @property
    def id(self) -> int:
        return self._id

    async def put_item(self, item: T) -> None:
        for subscription in self._subscriptions.values():
            await subscription.put(item)

    def subscribe(self, subscriber_id: int) -> asyncio.Queue[T]:
        self._subscriptions[subscriber_id] = asyncio.Queue()
        return self._subscriptions[subscriber_id]
