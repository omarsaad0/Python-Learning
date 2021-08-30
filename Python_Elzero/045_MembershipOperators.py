# Membership Operator

# String
name = "Omar"
print("s" in name)
print("a" in name)

print("|/" * 50)

# List

friends = ["Salah", "Haitham", "Reham"]

print("Osama" in friends)
print("Salah" in friends)
print("Reham" not in friends)
print("|/" * 50)

# USing in and not in in if condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Syria"]
countriesTwo = ["Italy", "USA"]

myCountry = input("State Your Country: ")
discountOne = 80
discountTwo = 20
discountThree = 50
if myCountry in countriesOne:
    print(f"Your Discount is {discountOne}")

elif myCountry in countriesTwo:
    print(f"Your Discount is {discountTwo}")

else:
    print(f"Your Discount is {discountThree}")


