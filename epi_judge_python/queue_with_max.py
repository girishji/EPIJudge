from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    def __init__(self) -> None:
        self.que = deque()
        self.maxq = deque()

    def enqueue(self, x: int) -> None:
        self.que.append(x)
        if not self.maxq:
            self.maxq.append(x)
        else:
            while self.maxq and self.maxq[-1] < x:
                self.maxq.pop()
            self.maxq.append(x)
        return

    def dequeue(self) -> int:
        if self.que[0] == self.maxq[0]:
            self.maxq.popleft()
        return self.que.popleft()

    def max(self) -> int:
        return self.maxq[0]
        return 0


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == "QueueWithMax":
                q = QueueWithMax()
            elif op == "enqueue":
                q.enqueue(arg)
            elif op == "dequeue":
                result = q.dequeue()
                if result != arg:
                    raise TestFailure(
                        "Dequeue: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "queue_with_max.py", "queue_with_max.tsv", queue_tester
        )
    )
