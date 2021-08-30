# Booolean Operators

# and

age = 23
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print("/|"* 50)

print(age > 16 or country == "Egypt" or rank > 0)  # True
print(age > 16 or country == "KSA" or rank > 0)  # True
print(age > 40 or country == "KSA" or rank < 0)  # False

print("/|"* 50)

print(age > 16) # True
print(not age > 16) # Not True = False

