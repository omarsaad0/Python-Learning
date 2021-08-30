# Practical

# Write Note
print("#"*80)
print("You Can Write The Full Letter or Full Name of The Time Unit".center(80, '#'))
print("#"*80)
# Collect Age Data
age = input("Please Write Your Age: ").strip()
# collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days").strip().lower()
# Get Time Unit
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':
    print("You Chose The Months")
    print(f"You Lived For {months:,} Months.")

if unit == 'weeks' or unit == 'w':
    print("You Chose The Weeks")
    print(f"You Lived For {weeks:,} Weeks")

if unit == 'days' or unit == 'd':
    print("You Chose The Days")
    print(f"You Lived For {days:,} Days.")
