from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque([])

    def enqueue(self, data) -> None:
        self.queue.append(data)

    def dequeue(self) -> None:
        return self.queue.popleft()
