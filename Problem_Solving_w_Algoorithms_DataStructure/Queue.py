class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return True if self.items == [] else False

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def look(self):
        return self.items


test = Queue()

test.enqueue('hello')
test.enqueue('dog')
test.enqueue(3)
test.dequeue()
print(test.look())
