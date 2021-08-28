class Skill:

    def __init__(self):
        self.skills = ["Python", "OpenCV", "Tensorflow"]  # Instance Attribute
        self.years_of_exp = 5

    def __str__(self):  # Magic Method

        return f"This is My Skills => {self.skills}"

    def __len__(self):  # Magic Method

        print(f"How many skills you have = {len(self.skills)}")
        return len(self.skills)


profile = Skill()
print(str(profile))
print(len(profile))

profile.skills.append("Deep Learning")
profile.skills.append("Computer Vision")
print("Years of Expience", profile.years_of_exp)
profile.years_of_exp +=2
print("Years of Expience", profile.years_of_exp)
print(len(profile))
#len(profile) # will execute what is inside the magic method which is the print of the lenght of the skills

#mystring = "Osama"
#print(type(mystring))
#print(mystring.__class__)

#print(dir(str))
