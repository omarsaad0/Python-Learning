# Control Flow if elif else

uname = "Omar"
uCountry = "KSA"
cname = "Python Course"
cPrice = 100
isStudent = "Yes"

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Libya":

    if isStudent == "Yes":
        print(f"Hello {uname} Because You are From {uCountry} And You're a Student")
        print(f"The Course \"{cname}\" Price is: {cPrice - 90}$")
    else:
        print(f"The Course \"{cname}\" Price is: {cPrice - 80}$")
        print(f"Hello {uname} Because You are From {uCountry}")

elif uCountry == "Kuwait" or uCountry == "Bahrain":

    print(f"Hello {uname} Because You are From {uCountry}")
    print(f"The Course \"{cname}\" Price is: {cPrice - 40}$")
elif uCountry == "Qatar":

    print(f"Hello {uname} Because You are From {uCountry}")
    print(f"The Course \"{cname}\" Price is: {cPrice - 30}$")
else:

    print(f"Hello {uname} Because You Are From {uCountry}")
    print(f"The Course \" {cname}\" Price Is: {cPrice-10}")
