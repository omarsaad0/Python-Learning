# Tuples ##################################

my_tuple = ("Omar", "Mohammed")
my_tuple2 = "Omar", "Mohammed"

print(my_tuple)
print(my_tuple2)
print(type(my_tuple))
print(type(my_tuple2))

# Tuple Indexing ##################################
my_tuple3 = (1, 2, 3, 4, 5)
print(my_tuple3[0])  # Indexing Same as list

# Tuple Assign Values ##################################

my_tuple4  = (1, 2, 3, 5)
#my_tuple4[2] = "Three"  #TypeError: 'tuple' object does not support item assignment

# Tuple Items ##################################

# Tuple with one element

my_tuple5 = ("Omar",)  # , makes a tuble
my_string = ("Omar")

print(type(my_tuple))
print(type(my_string))

# Tuple Concatenation

a = (1, 2, 3, 4, 5)
b = (5, 6)
c = a + b
d = a + ("A", "B", True) + c
print(c)
print(d)

# Tuple, List, String Repeat (*)

mystring = "omar"
myList = [1, 2]
my_tuple6 = (1, 2)
print(mystring*5)

# Method => count()
a = (1, 3, 4, 5, 1, 6, 5, 1)
print(a.count(1))

# Method => index()

b = (1, 3, 7, 5, 6)
print("The Position of Index is: {:d}".format(b.index(5)))
print(f"The Position of Index is: {b.index(5)}")

# Tuple Destruct

a = ("A", "B", "C")
#x, y, z = "A", "B", "C"  # or another way
x, y, z = a  # Packing the tuple to 3 variable
print(x)
print(y)
print(z)




























#
