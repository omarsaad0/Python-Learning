# Control Flow if elif else

uname = "Omar"
uCountry = "Qatar"
cname = "Python Course"
cPrice = 100

if uCountry == "Egypt":
     print(f"Hello {uname} Because You are From {uCountry}")
     print(f"The Course \"{cname}\" Price is: {cPrice - 80}$")

elif uCountry == "KSA":

    print(f"Hello {uname} Because You are From {uCountry}")
    print(f"The Course \"{cname}\" Price is: {cPrice - 60}$")
elif uCountry == "Kuweit":

    print(f"Hello {uname} Because You are From {uCountry}")
    print(f"The Course \"{cname}\" Price is: {cPrice - 40}$")
elif uCountry == "Qatar":

    print(f"Hello {uname} Because You are From {uCountry}")
    print(f"The Course \"{cname}\" Price is: {cPrice - 30}$")
else :

    print(f"Hello {uname} Because You Are From {uCountry}")
    print(f"The Course \" {cname}\" Price Is: {cPrice-10}")

