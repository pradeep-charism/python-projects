from collections import deque

a = [1, 5, 3, 9, 7, 2, 50, 3, 3]
print(a)
a.pop(2)
print(a)
print(a.index(5))
print(a.count(3))

a.sort(key=None, reverse=True)
print(a)

queue = deque(["red", "blue", "green"])
print(queue)
queue.append("yellow")
queue.append("purple")
queue.append("white")
print(queue)
print(queue.pop())
print(queue.popleft())

# List comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

# Tuple
result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(result)

var = [(x, x ** 2) for x in range(6)]
print(var)

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for elem in vec for num in elem]
print(result)

# Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

'orange' in basket  # fast membership testing

'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)  # unique letters in a

print(a - b)  # letters in a but not in b

print(a | b)  # letters in a or b or both

print(a & b)  # letters in both a and b

print(a ^ b)  # letters in a or b but not both

# Dict
tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel.keys())

sorted(tel.keys())

print('guido' in tel)
print('jack' not in tel)

# dict comprehensions
print({x: x ** 2 for x in (2, 4, 6)})

# Looking techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# Reversed
for i in reversed(range(1, 10, 2)):
    print(i)


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


print(times_tables())
print([i * j for i in range(10) for j in range(10)])
print(times_tables() == [i * j for i in range(10) for j in range(10)])

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50]  # Display first 50 ids


