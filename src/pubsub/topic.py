import queue


class Topic:
    def __init__(self, id: int) -> None:
        self._id = id
        self._subscriptions: dict[int, queue.Queue] = {}

    @property
    def id(self) -> int:
        return self._id

    def put_item(self, item: str) -> None:
        for subscription in self._subscriptions.values():
            subscription.put(item)

    def subscribe(self, subscriber_id: int) -> queue.Queue:
        self._subscriptions[subscriber_id] = queue.Queue()
        return self._subscriptions[subscriber_id]
