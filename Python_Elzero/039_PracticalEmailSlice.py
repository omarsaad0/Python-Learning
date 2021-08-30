# Practical Email Slice


# email = "omarsaad2411@gmail.com"

the_name = input("What\' Your Name ? ").strip().capitalize()
the_email = input("What\' Your Email ? ").strip().capitalize()
the_username = the_email[:the_email.index("@")].strip().capitalize()
the_domain = the_email[the_email.index("@")+1:].strip()
print(f"Hello {the_name} Your Email is {the_email}")
print(f"Your Username Is {the_username} \nYour Website Is {the_domain} ")
