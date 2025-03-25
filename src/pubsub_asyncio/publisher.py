from typing import Generic, TypeVar

from topic import Topic

T = TypeVar("T")


class Publisher(Generic[T]):
    def __init__(self, id: int) -> None:
        self._id = id

    async def publish(self, topic: Topic[T], item: T) -> None:
        await topic.put_item(item)
