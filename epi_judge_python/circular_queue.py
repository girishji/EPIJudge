from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools


class Queue:
    def __init__(self, capacity: int) -> None:
        self.fr = self.ba = 0
        self.cap = max(1, capacity)
        self.que = [0] * self.cap
        return

    def __resize(self):
        temp = [0] * (2 * self.cap)
        for i in range(self.fr, self.cap):
            temp[i - self.fr] = self.que[i]
        for i in range(0, self.fr):
            temp[i + self.cap - self.fr] = self.que[i]
        self.fr = 0
        self.ba = self.cap - 1
        self.cap *= 2
        self.que = temp

    def enqueue(self, x: int) -> None:
        if (self.fr == 0 and self.ba == self.cap - 1) or (self.fr - self.ba == 1):
            self.__resize()
        self.que[self.ba] = x
        self.ba = 0 if self.ba == self.cap - 1 else self.ba + 1
        return

    def dequeue(self) -> int:
        if self.fr == self.ba:
            raise IndexError()
        elem = self.que[self.fr]
        self.que[self.fr] = 0
        self.fr = 0 if self.fr == self.cap - 1 else self.fr + 1
        return elem

    def size(self) -> int:
        return (
            self.ba - self.fr if self.ba >= self.fr else self.cap - (self.fr - self.ba)
        )


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure("Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
