import random
import string
import time

start = time.time()


def str_gen (l):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range (l)))
    print(result)
    return 0


string_gen = ''
while string_gen != 'methinksitslikeaweasel':
    string_gen = str_gen(22)

time.sleep(1)
end = time.time()
print(f"Found The String in {end-start}")
