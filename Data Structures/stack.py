class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):

        self.first = None

    def push(self, item):

        item = Node(item)

        if not self.first:
            self.first = self.last = item

        else:
            old_first = self.first
            self.first = item
            self.first.next = old_first

    def pop(self):

        c = self.first

        if c:
            item = c
            self.first = c.next
            return item.item

    def traveler(self):

        c = self.first

        while c:
            print(c.item)
            c = c.next
