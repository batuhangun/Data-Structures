class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Deque:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def push_head(self, k):

        k = Node(k)

        if not self.head:
            self.head = self.tail = k

        else:
            old_head = self.head
            self.head = k
            self.head.next = old_head

        self.size += 1

    def push_tail(self, k):

        k = Node(k)

        if not self.head:
            self.head = self.tail = k

        else:
            self.tail.next = k

        self.size += 1

    def pop_head(self):

        self.head = self.head.next
        self.size -= 1

    def pop_tail(self):

        curr = self.head
        c = 0
        while c < self.size - 1:
            curr = curr.next
            c += 1

        self.tail = curr
        curr.next = None
        self.size -= 1

    def traveler(self):

        c = 0
        curr = self.head

        while c < self.size:
            yield curr.item
            curr = curr.next
            c += 1
