# Ternary Conditional Operational

country = "Egypt"

if country == "Egypt":

    print(f"The Weather in {country} is 15 degree")

elif country == "KSA":

    print(f"The Weather in {country} is 25 degree")

else:
    print(f"The weather in {country} is Not Found")


# Short if

movieRate = 18
age = 16

if age < movieRate:
    print("Movie Is Not Good For U")  # Condition if True
else:
    print("Movie Is Good For U, Happy Watching")  # Condition if False

Test1 = "Movie Is Not Good For u" if age < movieRate else "Movie is Good For U, And Happy Watching"
print(Test1)

# Condition if True | if Condition | Else | Condition if Else
