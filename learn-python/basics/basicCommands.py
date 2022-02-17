print("Thank you Jesus")

# Read a value from standard input a value
# input("Thank you")


# Evaluate expression
x = 1
print(x)
x += 3
print(x)

# loops
if x > 1:
    print("great than 1")
else:
    print("less than 1")

n = 3
while n > 1:
    print(n)
    n -= 1

# Arithmetic operator
print({100 % 3}, {100 / 3})

z = 1
print(z, type(z))
z = "dsf"
print(z, type(z))

print(17 // 3)  # floor division discards the fractional part
print(5 ** 2)  # 5 squared

# use raw strings by adding an r before the first quote
print(r'C:\some\name')

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''
print("""\
      dsfdsfds
      ddsf
      dfdf
      dfdfds
      """)

w = 'thanks'
print(w[:3] + w[3:])

# All slice operations return a new list containing the requested elements.
# This means that the following slice returns a new (shallow) copy of the list:
squares = [1, 4, 9, 16, 25]
for n in squares:
    print(n, end='-')
    if n == 16:
        squares.insert(n, 100)

print('\n')

print(squares[:])
squares.append(10)
print(squares[:])
squares = []
print(squares[:])

# Fibonacci
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b

# Fibonacci
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

print('\n')
# Loops
for i in range(3, 15, 4):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))


def f(ab, l=[]):
    l.append(ab)
    return l


print(f(1))
print(f(2))
print(f(3))

# if __name__ == "__main__":
#     import sys
#
#     print(int(sys.argv[1]))


import sys
print(dir(sys))

print('12'.zfill(5))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))

# Formatting: https://docs.python.org/3.6/tutorial/inputoutput.html




quit(1)
