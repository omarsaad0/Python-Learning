# List Method

myFriends = ["A", "B", "C", "D", "E"]
myOldFriends = ["X", "Y", "Z"]
myFriends.append(3)
print(myFriends)
myFriends.append(myOldFriends)  # As a one element
print(myFriends)
print(myFriends[6][2])  # Two Parenthesis

# Extend

a = [1, 2, 3, 4]
b = ["I", "J", "K"]

a.extend(b)  # Concatenate the two lists as one list not nested lists
print(a)

a.remove("J")
print(a)

y = [1, 500, 20, 600, 12, 65 , 420]
y.sort(reverse=True)
print(y)

z = [200, 500, "Omar", 6, 450]
z.reverse()
print(z)

