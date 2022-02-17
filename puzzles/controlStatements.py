def odd_even(number):
    print("Odd/Even numbers")
    for i in range(number):
        if i % 2 == 0:
            print(i, "is a event number")
            continue
        else:
            print(i, "is a odd number")


def fibonacci(number):
    print("\nFibonacci numbers")
    result = []
    a, b = 0, 1
    while b < number:
        print(b, end=", ")
        a, b = b, a + b
        result.append(b)
    return result


def primenumbers():
    print("\n\nPrime numbers")
    for n in range(2, 10):
        for m in range(2, n):
            if n % m == 0:
                break
        else:
            print(n)


odd_even(5)
fibonacci(10)
primenumbers()

f = fibonacci
print(f(100))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

print(list(zip(*matrix)))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
