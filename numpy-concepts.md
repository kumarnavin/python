# NumPy notes

>>> It works on arrays >>>
import numpy as np

np.zeros(10) —creates 10 zeroes
np.ones(10) * 5 —creates 10 5’s
np.arange(10,51) — int from 10 to 50
np.arange(10,51,2) — even int
np.arange(9).reshape(3,3) —create 3*3 matrix
np.eye(3) —create 3*3 identity matrix
np.random.rand(1) —random number between 0 and 1
np.random.randn(25) — array of 25 random numbers
np.arange(1,101).reshape(10,10) / 100
np.linspace(0,1,20) — Create an array of 20 linearly spaced points between 0 and 1
mat = np.arange(1,26).reshape(5,5) —convert a flat array into 5*5

mat[2:,1:] — slice where row num 2+, column num 1+
mat.sum()
mat.sum(axis=0) — sum for all columns for each row
mat.std() —stddev

## Set up matrix
arr2d = np.zeros((10,10))
arr2d[[2,4,6,8]] —selects 4 indexed rows
#Allows in any order
arr2d[[6,4,2,7]]
arr = np.arange(1,11) — array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr > 4 — array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)
bool_arr = arr>4 — store into an array
arr[bool_arr] — array([ 5,  6,  7,  8,  9, 10])
arr[arr>2]
arr + arr — adds the numbers by individual index
arr**3 — power of 3 for every element
np.sqrt(arr) — sort of every element
np.max(arr) — picks the max element
