#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cnvt = str(number)
chk =  cnvt[-1:]
if int(chk) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, chk))
elif int(chk) == 0:
    print("Last digit of {} is {} and is 0".format(number, chk))
elif int(chk) < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, chk))
    if int(chk) == -98:
        print("Last digit of {} is -8 and is less than 6 and not 0".format(number, chk))
else:
    pass
