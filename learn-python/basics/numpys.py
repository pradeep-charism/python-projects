import numpy as np

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)

print(a5.shape)
print(a1.shape)


old = np.array([[1, 1, 1], [1, 1, 1]])
print(old)
new = old
new[0, :2] = 0

print(old)

