# Set

# Set items are enclosed in curly braces
# Set are not ordered nor indexed
# Set can not be sliced
# Only mutable data types Not list/dict
# Set Items are Unique
mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
#print(mySetOne[0])

mySetTwo = {1, 2, 3, 4, 5}
#print(mySetTwo[:3])

mySetThree = {"Omar", 100, 100.5, True, (1, 2, 3)}  # Un hashable type: 'list' Only mutable data types Not list/dict
print(mySetThree)

mySetFour = {1, 2, "Osama", "Omar", "Osama", 1}  # Does not repeat the items (Unique)
print(mySetFour)
