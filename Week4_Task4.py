# Replace all odd numbers in an array of 1-10 with the value -1

import numpy as np
a = np.arange(1,11)
b = np.where(a%2 == 0, a, -1)
print(b)