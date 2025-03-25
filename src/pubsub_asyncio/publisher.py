from topic import Topic


class Publisher:
    def __init__(self, id: int) -> None:
        self._id = id

    async def publish(self, topic: Topic, item: str) -> None:
        await topic.put_item(item)
