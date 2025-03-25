import queue
import threading

from topic import Topic


class Subscriber:
    def __init__(self, id: int) -> None:
        self._id = id

    def subscribe(self, topic: Topic) -> queue.Queue:
        q = topic.subscribe(subscriber_id=self._id)
        threading.Thread(target=self._worker, args=[q], daemon=True).start()
        return q

    def _worker(self, q: queue.Queue) -> None:
        while True:
            item = q.get()
            print(f"Subscriber {self._id}: working on {item}")
            q.task_done()
