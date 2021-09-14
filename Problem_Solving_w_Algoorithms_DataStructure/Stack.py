class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)    # .insert will be used with index 0 if we choose the end is the beginning of the list
        #print(f"{item} is added to the stack")

    def pop(self):
        return self.items.pop()    # Index 0 if we chose the end is at beginning of the list

    def peek(self):
        return self.items[len(self.items)-1]  # Index 0 if we ....

    def size(self):
        return len(self.items)


s = Stack()
'''
s.push(5)
s.push("Hi")
s.push("Test")
s.pop()
s.peek()
print(s.size())
print(s.is_empty())
'''
########################################################################################################################


def par_checker (symbol_string):
    balanced = True
    for i in symbol_string:

        if i == '(' or i =='[' or i =='{':
            s.push(i)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

    return print(f'Is The String Balanced ? {balanced}')

par_checker('()()()()()()()((()))[]{}}')