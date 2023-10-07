import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
arr = np.array([1, 2, 3, 4, 5])
s3 = pd.Series(arr, ['a', 'b', 'c', 'd', 'e'])
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s4 = pd.Series(d)

