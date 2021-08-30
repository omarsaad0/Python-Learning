############


my_list = ["One", "Two", "One", 1, 100.5, True]

print(my_list)
print(my_list[1])

print(my_list[1:4])
print(my_list[:4:2])

my_list[1] = 2

print(my_list)

my_list[-1] = False

my_list[0:2] = []
print(len(my_list))