class ListIsEmptyError(Exception):
    pass


class Fifo:
    def __init__(self, limit=5):
        self.limit = limit
        self.counter = 0
        b = a = FifoItem()
        for i in range(self.limit-1):
            a = FifoItem(next=a)
        b.next = a
        self.head = a
        self.tail = a

    def push(self, value=None):
        if self.tail == self.head and self.counter:
            self.pop()

        self.tail.value = value
        self.tail = self.tail.next

        self.counter = min(self.limit, self.counter + 1)

    def pop(self):
        if self.head.value is None:
            raise ListIsEmptyError

        buff = self.head.value
        self.head.value = None
        self.head = self.head.next
        self.counter = max(0, self.counter - 1)
        return buff


class FifoItem:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


if __name__ == '__main__':
    a = Fifo(3)
    a.push(1)
    a.push(2)
    a.push(3)
    assert a.pop() == 1
    a.push(4)
    assert a.pop() == 2
