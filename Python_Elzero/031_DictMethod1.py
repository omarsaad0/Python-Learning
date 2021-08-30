# Dict Method

# clear() ######################################################################

user = {
    "name": "omar"
}
print(user)
user.clear()
print(user)

print("/|"*50)

# update() #####################################################################

member = {
    "name": "Omar",
    "age": 23
}
print(member)
member["gender"] = "male"
print(member)
member.update({"country":"Egypt", "MS": "Not Yet"})
print(member)
print("/|"*50)
# copy() ######################################################################

main = {
    "name": "Hoyam"
}

b = main.copy()
print(b)
main.update({"skills": "python"})
print(main)
print(b)


# keys() + values()

print(main.keys())
print(main.values())
print("/|"*50)
########################################################################################################################

# setdefault() ################################################################

user1 = {
    "name": "omar"
}
print(user1)
print(user1.setdefault("name", "Hoyam"))  # if the key exist then it will print the value if not will update a key and the value
print(user1)
print("/|"*50)

# popitem()

member1 = {
    "name": "Omar",
    "age": "23"
}
print(member1)
member1.update({"Skills": "None"})
print(member1.popitem())  # Return the last inserted item
print("/|"*50)

# items()  ###################################################################

view = {
    "name": "omar",
    "skills": "none"
}
allItems = view.items()  # both keys and values tuples inside a big list
print(view)
view["age"] = 23
print(allItems)
print("/|"*50)

# fromkeys()  ################################################################

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "x"
print(dict.fromkeys(a, b))  # create a dict from keys (a) and values (b)
