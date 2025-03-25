from typing import TypeVar

from topic import Topic

T = TypeVar("T")


class Publisher:
    def __init__(self, id: int) -> None:
        self._id = id

    def publish(self, topic: Topic[T], item: T) -> None:
        topic.put_item(item)
