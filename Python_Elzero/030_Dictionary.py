# Dictionary

# Curly braces
# Has Key and value
# Immutable data types for Key (Number, String, Tuple) List is not allowed
# Dict value can be any data type
# Dict key must be unique
user = {
    "name": "Osama",
    "age": 36,
    "Country": "Egypt",
    "skills": ["Html", "css", "Js"],
    "rating": 2
}
print(user)  # name is overwritten because name is used twice

print(user["Country"])

print(user.get("Country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary Nested Dictionary

languages = {
    "one": {
        "name": "Html",
        "progress": "80%"
    },
    "two": {
        "name": "Python",
        "progress": "50%"
    }
}
print(languages)
print(languages["one"])
print(languages["two"]["progress"])

# Dictionary Length

print(len(languages))  # Two elements only
print(len(languages["two"]))

frameworkOne = {
    "name": "Tensorflow",
    "progress": "50%",
}
frameworkTwo = {
    "name": "Pytorch",
    "progress": "20%",
}
frameworkTwo = {
    "name": "Theano",
    "progress": "10%",
}

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo
}
print(allFramework)