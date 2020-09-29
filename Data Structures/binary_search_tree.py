class Node:

    def __init__(self, v):
        self.value = v
        self.right = None
        self.left = None


class BST:

    def __init__(self):

        self.root = None
        self.size = 0

    def push(self, v):
        node = Node(v)

        if not self.root:
            self.root = node
        else:
            curr = self.root
            while curr:
                if node.value <= curr.value:
                    if not curr.left:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                elif node.value > curr.value:
                    if not curr.right:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    def get(self, v):

        curr = self.root
        prev = self.root

        while curr:
            if curr.value < v:
                prev = curr
                curr = curr.right
            elif curr.value > v:
                prev = curr
                curr = curr.left
            else:
                return curr, prev
        return False

    def min_value(self):

        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.value

    def max_value(self):

        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.value

    def delete_min(self):

        curr = self.root
        prev = self.root

        while curr.left:
            prev = curr
            curr = curr.left

        if curr == self.root:
            self.root = self.root.right
        elif curr.right:
            prev.left = curr.right
        else:
            prev.left = None

    def get_min_node(self, node):

        curr = node
        prev = node
        while curr.left:
            prev = curr
            curr = curr.left
        return curr, prev

    def delete(self, v):

        curr, prev = self.get(v)

        if curr.right and curr.left:
            min_, prev_min_ = self.get_min_node(curr.right)
            if curr.value < prev.value:
                prev_min_.left = min_.right if min_.right else None
                prev.left = min_
                min_.left = curr.left
                min_.right = curr.right

            else:
                prev_min_.left = min_.right if min_.right else None
                prev.right = min_
                min_left = curr.left
                min_.right = curr.right

    def traveler(self, curr):

        curr = curr
        if curr:
            self.traveler(curr.left)
            print(curr.value)
            self.traveler(curr.right)
