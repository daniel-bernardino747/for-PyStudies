import numpy as np
import pandas as pd

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
lis = np.array([1, 2, 3, 4, 5, 6, 7, 8])

ser = pd.Series(dic, index=['a', 'b', 'c', 'd'], dtype=float, name='Test-01')

print("\nIs a copy. Don't chance the original list 'lis':")
res = pd.Series(lis, name='Test-02.1', copy=True)
res.loc[0] = 999

print(lis)
print(res)

print("\nChance the original list 'lis':")
res = pd.Series(lis, name='Test-02.2', copy=False)
res.loc[0] = 999

print(lis)
print(res)
