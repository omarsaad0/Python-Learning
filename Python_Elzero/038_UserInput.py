# User Input

#input("Hello Python")

fname = input("What\'s is Your First Name?")
mname = input("What\'s is Your Middle Name?")
lname = input("What\'s is Your Last Name?")

fname = fname.strip().capitalize()  # To Remove the White spaces between names And Capitalize First letter
lname = lname.strip().capitalize()

print(f"Hello {fname} {mname.strip().capitalize():.1s} {lname} Happy To See You")

