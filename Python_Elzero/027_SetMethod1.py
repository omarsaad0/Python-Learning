# Set Method

# clear()

a = {1, 2, 4}
a.clear()
print()


# union() Because sets dont support concatenate ############################################

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
z = ("Zero", 0)
#print(b + c)  # error unsupported operand type(s) for +: 'set' and 'set

print(b | c)
print(b.union(c,z))

# add() ############################################

d = {1, 2, 3, 5}
d.add(5)
d.add(8)
print(d)
print("#"*10)

# copy() ############################################

e = {1, 2, 3, 9}
f = e.copy()
print(e)
print(f)
e.add(5)
f.add(10)
print(e)
print(f)

# remove() Error if the value is not there  ############################################

g = {1, 2, 3, 4, 8}
g.remove(2)
print(g)

# discard() Deos not give an error if the value is not there  ############################################

h = {1, 2, 3, 4, 8}
h.discard(28582)
print(h)

# pop() remove random element  ############################################


# update ############################################

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(k)
j.update((["Html", "CSS"]))
print(j)

# difference() ############################################

a = {1, 2, 3, 4}
b = {1, 2, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # == a - b
print(a)
print("/|"*40)

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
print(c.difference_update(d))  # == a - b  Update the original set with the difference (difference then update)
print(c)
print("/|"*40)

# intersection ############################################

# e & f return the intersections between the two sets

# intersection_update ############################################

# symmetric_difference() ############################################
# returns the not intersected elements
i = {1, 2, 3, 4, 5}
j = {"omar", "Zero", 1, 2, 4}
print(i.symmetric_difference(j))  # i ^ j
print(i)
print(j)
print("/|"*40)
# symmetric_difference_update() ###########################################


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

# issuperset() ###########################################
# if the elements has has the same elements in the original set then it returns true

a = {1, 2, 3, 4}
b = {1, 2, 4}
d = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
print(a.issuperset(d))  # False

print("/|"*40)

# issubset()
# True if the set contains all elements that in the original set

print("/|"*40)

# isdisjoint()
# returns true if there is no elements alike in both sets
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}
print(g.isdisjoint(h))
print(g.isdisjoint(i))