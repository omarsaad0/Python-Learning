# String Formatting New Ways

name = "Omar"
age = 23
rank = 4


print("My Name Is: {:s}, My Age Is {:d} and My Rank Is {:.2f}".format(name, age, rank))

myLongString = "Hello People of Elzero Web School I Love You"

print("Message is: {:.13s}" .format(myLongString))


# Format Money

my_money = 500162350198

print("My Money in Bank Is: {}".format(my_money))
print("My Money in Bank Is: {:_d}".format(my_money))
print("My Money in Bank Is: {:,d}".format(my_money))

# Rearrange Items

a, b, c = "One", "Two", "Three"

print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One

x, y, z = 10, 20, 30

print("Hello {} {} {}".format(x, y, z))  # Hello One Two Three
print("Hello {1:d} {2:d} {0:.2f}".format(x, y, z))  # Hello Two Three One


# Format in Version 3.6+

myName = "omar"
myAge = 23
print("My Name is {myName} And My Age Is: {myAge}")
print(f"My Name is {myName} And My Age Is: {myAge}")
