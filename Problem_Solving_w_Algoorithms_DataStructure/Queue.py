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
'''
test.enqueue('hello')
test.enqueue('dog')
test.enqueue(3)
test.dequeue()
print(test.look())
'''

def hot_potato(name_list, num):

    hot_queue = Queue()

    for i in name_list:
        hot_queue.enqueue(i)

    while hot_queue.size()>1:

        for i in range(num):
            removed = hot_queue.dequeue()
            hot_queue.enqueue(removed)
        hot_queue.dequeue()

    return hot_queue.look()


print(hot_potato(["Omar", "Salah", "Fekry", "Haitham", "Nabawy", "Eman", "Mahmoud", "Adham"], 9))