class Member:
    not_allowed_name = ["Shit", "Hell", "Baloot"]
    users_num = 0

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

        Member.users_num += 1

    @classmethod
    def show_users_count(cls):

        print(f"We Have {cls.users_num} Users In Our System.")

    @staticmethod
    def say_hello():  # static method not linked to class or instances

        print(f"Hello From Static Method")

    def full_name(self):  # instance method

        if self.fname in Member.not_allowed_name:
            raise ValueError("Name is Not Allowed")

        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def welcome(self):

        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname}"
        else:
            return f"Hello {self.fname}"

    def get_all_info(self):

        return f"{self.welcome()}, Your Full Name Is: {self.full_name()}"

    def delete_user(self):

        Member.users_num -= 1

        return f"Users {self.fname} Is Deleted"


print(Member.users_num)
member_one = Member("Osama", "Mohammed", "Elzero", "Male")
member_two = Member("Mohammed", "Mohammed", "Saad", "Male")
member_three = Member("Hala", "Mohammed", "Saad", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.mname)
# print(member_three.lname)

# print(member_one.full_name())
# print(member_three.welcome())

# print(dir(Member))

# print(member_three.get_all_info())
# print(member_four.get_all_info())  # Value Error
print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)

print("#" * 100)

Member.show_users_count()
Member.say_hello()
#print("#" * 100)

#print(member_three.full_name())  # Both same
#print(Member.full_name(member_three))  # Both same (Backend)


