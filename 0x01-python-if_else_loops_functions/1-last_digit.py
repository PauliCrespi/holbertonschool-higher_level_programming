#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
inumber = number
if number < 0:
    inumber = number * -1
lastdigit = inumber % 10
if number < 0:
        lastdigit = lastdigit * -1
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and \
is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdigit))
elif lastdigit != 0 and lastdigit < 6:
    print("Last digit of {:d} is {:d} and \
is less than 6 and not 0".format(number, lastdigit))