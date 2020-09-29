class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):

        self.first = None
        self.tail = None
        self.size = 0

    def lenght(self):

        return self.size

    def add(self, item):

        item = Node(item)

        if not self.first:
            self.first = self.tail = item
            self.size += 1

        else:
            self.tail.next = item
            self.tail = item
            self.size += 1

    def add_k_node(self, item, n):

        item = Node(item)

        if n == 0:
            old_first = self.first
            self.first = item
            self.first.next = old_first

        else:
            curr = self.first
            for i in range(n - 1):
                curr = curr.next

            item.next = curr.next
            curr.next = item
        self.size += 1

    def delete(self, n):

        if n == 0:
            self.first = self.first.next
            self.size -= 1

        else:
            curr = self.first

            for i in range(n - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1

    def find(self, k):

        curr = self.first
        boolen = False
        c = 0

        while not boolen and c < self.size:

            if curr.item == k:
                boolen = True
            else:
                curr = curr.next
            c += 1

        return boolen

    def max_k(self):

        c = 0
        l = []
        curr = self.first

        while c < self.size:
            l.append(curr.item)
            curr = curr.next
            c += 1

        return max(l)

    def traveler(self):

        curr = self.first
        c = 0

        while c < self.size:
            yield curr.item
            curr = curr.next
            c += 1
