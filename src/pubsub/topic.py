import queue


class Topic:
    def __init__(self) -> None:
        self._subscriptions: dict[int, queue.Queue] = {}

    def put_item(self, item: str) -> None:
        for subscription in self._subscriptions.values():
            subscription.put(item)

    def subscribe(self, subscriber_id: int) -> queue.Queue:
        self._subscriptions[subscriber_id] = queue.Queue()
        return self._subscriptions[subscriber_id]
