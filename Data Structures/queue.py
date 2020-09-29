class Node:

    def __init__(self, item):
        self.item = item
        self.previous = None


class Queue:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):

        if not self.head:
            item = Node(item)
            self.head = self.tail = item
            self.size += 1

        else:
            item = Node(item)
            self.tail.previous = item
            self.tail = item
            self.size += 1

    def dequeue(self):

        if self.size:
            c = self.head
            self.head = self.head.previous
            self.size -= 1
            return c.item

    def size_alt(self):

        count = 0
        c = self.head

        while c:
            count += 1
            c = c.previous
        return count

    def traveler(self):

        c = self.head

        while c:
            print(c.item)
            c = c.previous
