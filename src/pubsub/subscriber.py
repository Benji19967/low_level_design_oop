import queue
import threading
import time

from topic import Topic


class Subscriber:
    def __init__(self, id: int) -> None:
        self._id = id
        self._subscriptions: dict[int, queue.Queue] = {}

    def subscribe(self, topic: Topic) -> queue.Queue:
        q = topic.subscribe(subscriber_id=self._id)
        threading.Thread(target=self._worker, args=[q], daemon=True).start()
        self._subscriptions[topic.id] = q
        return q

    def unsubscribe(self, topic: Topic):
        q = self._subscriptions[topic.id]
        q.put(None)

    def _worker(self, q: queue.Queue) -> None:
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                return
            # print(f"Subscriber {self._id}: working on {item}")
            time.sleep(0.1)
            q.task_done()
