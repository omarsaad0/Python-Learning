# List Method 2

# clear() ################################

a = [1, 2, 3, 4]

a.clear()

print(a)

# copy() ################################

b = [1, 2, 3, 4, 5]
c = b.copy()
print(b)  # Main List
print(c)  # Copied List
# Shallow Copy is to that the copied list is separated from the main list
b.append(6)
print(b)  # Main List
print(c)  # Copied List

# count() ################################

d = [1, 2, 3, 4, 5, 6, 1, 2, 1]
print(d.count(1))  # Print the count of the number

# index() ################################

print(d.index(4))  # Finds the index of the value in the list

# insert() ################################

f = [1, 2, 3, 4, 5, 6, "A", "B"]
f.insert(0, "Test")  # Insert Object Before Index
f.insert(-1, "Test")
f.insert(4, 4)
print(f)

# pop() ################################

g = [1, 2, 3, 4]
print(g.pop(2))  # Remove the element and return it (index)
print(g)
