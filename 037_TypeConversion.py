# Type Conversion


# str() ###########################################################################

a = 10
print(type(a))
print(type(str(a)))
print("/|"*50)

# tuple()

c = "Omar"  # string
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dict

print(tuple(c))
print(tuple(d))
print(tuple(e)) # Random elements 
print(tuple(d))
print("/|"*50)
# list()

c = "Omar"  # string
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dict

print(list(c))
print(list(d))
print(list(e))  # Random elements
print(list(d))
print("/|"*50)
# set()

c = "Omar"  # string
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # Set
f = {"A": 1, "B": 2}  # Dict

print(set(c))  # Random elements
print(set(d))  # Random elements
print(set(e))  # Random elements
print(set(d))  # Random elements

print("/|"*50)

# dict()

#c = "Omar"  # string
d = (("A", 1), ("B", 2), ("C", 3))  # To Convert Tuple to Dict make it nested tuple to take the Key + Value
e = [["One", 1], ["Two", 2], ["Three", 3]]  # To Convert List to Dict make it nested List to take Key + Value
f = {{"A", 1}, {"B", 2}}  # Can not be converted to Dict

#print(dict(c))  # Can not be Converted to Dict bec no Key + Value
print(dict(d))
print(dict(e))
print(dict(d))  # Un hashable Type 'set'
