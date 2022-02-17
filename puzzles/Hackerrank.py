#!/bin/python3

def is_leap(year):
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap


print(is_leap(1990))

quit()


def isEven(number):
    if number % 2 == 0:
        return True


if __name__ == '__main__':
    n = int(input().strip())

if isEven(n) and 2 <= n <= 5:
    print("Not Weird")
elif isEven(n) and 6 <= n <= 20:
    print("Weird")
elif isEven(n) and n > 20:
    print("Not Weird")
else:
    print("Weird")
