#########Summing a List Elements Using Recursion############

def summing(list1):
    if not list1:
        return 1
    else:
        return list1[0] + sum(list1[1:])


print(summing([1, 2, 3, 6, 4, 8, 88, 55, 16, 86]))


def count(list2):
    if not list2:
        return 1
    else:
        return 1 + count(list2[1:])


print(count([1, 5, 8, 6, 1])-1)  # -1 because the index starts from 0, or IDK :)


def max_number(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_number(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max_number([1, 5, 180, 150, 1080, 960, 181, 545, 20]))
