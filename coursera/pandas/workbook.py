import numpy as np
import pandas as pd

students = ['Alice', 'Bob', 'Carol', None]
pd.Series(students)

numbers = [1, 2, 3, 5, 4, 6, 2.3, None]
pd.Series(numbers)

np.nan == None
np.nan == np.nan
np.isnan(np.nan)

# Dictionary
students_scores = {
    "Alice": 'Maths',
    'Bob': 'English', 'Charlie': 'Physics'
}

s = pd.Series(students_scores)
s

students_scores = {
    "Alice": 'Maths',
    'Bob': 'English',
    'Charlie': 'Physics'
}

sid = pd.Series(students_scores, index=['a', 'b', 'Bob'])
sid


# Tuples
students_tp = [('a', 'a1'), ('b1', 'b2')]
st = pd.Series(students_tp)
st

s = pd.Series(['Physics', 'Maths', 'English'], index=['Alice', 'Bob', 'Charlie'])
s



