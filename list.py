class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkedList:
    def __init__(self):
        pass

    def __str__(self):
        """Print entire linked list."""
        pass

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def insert_at_head(self, node):
        pass

    def insert_or_overwrite_value(self, value):
        pass






if __name__ == "__main__":
    l = LinkedList()
    print(l)
    for i in range(5):
        l.insert_at_head(Node(i))
    print(l)
    print(l.delete(2))
    print(l)
    print(l.delete(4))
    print(l)
    print(l.delete(0))
    print(l)

    print(l.find(0))
    print(l.find(3))
    print(l.find(1))

    l.insert_or_overwrite_value(4)
    print(l)
    l.insert_or_overwrite_value(4)
    print(l)