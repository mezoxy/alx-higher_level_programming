#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = int(str(number)[-1])
else:
    last_digit = int(str(number)[-1]) * -1
print(f"Last digit of {number:d} is", end=" ")
if last_digit > 5:
    print(f"{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit} and is 0")
else:
    print(f"{last_digit} and is less than 6 and not 0")
