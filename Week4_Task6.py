# Create two arrays a and b, stack these two arrays vertically,
#  use the  np.dot and np.sum to calculate totals


import numpy as np
a = np.arange(1,17).reshape(4,4)
b = np.arange(11,27).reshape(4,4)
c = np.dot(a,b)
print(c)
sum = np.sum(c)
print(sum)