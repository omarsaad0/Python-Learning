import random


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


class Printer:

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate


class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


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


#print(hot_potato(["Omar", "Salah", "Fekry", "Haitham", "Nabawy", "Eman", "Mahmoud", "Adham"], 9))

###################################################Printer Simulation###################################################


def simulation(num_seconds, pages_per_minute):

    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_time = []

    for current_seconds in range(num_seconds):

        if new_print_task():

            task = Task(current_seconds)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):

            next_task = print_queue.dequeue()
            waiting_time.append(next_task.wait_time(current_seconds))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    average_wait = sum(waiting_time) / len(waiting_time)
    print(f"Average Wait {average_wait} secs {print_queue.size()} Tasks Remaining")


def new_print_task():

    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range (10):
    simulation(3600, 10)
