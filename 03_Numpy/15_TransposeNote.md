# NumPy Transpose

### What is Transpose?

Transpose is the operation of changing the arrangement of an array so that rows become columns and columns become rows.

For a 2D array:

Original:
1  2  3
4  5  6

Transpose:
1  4
2  5
3  6

The shape changes from `(2, 3)` to `(3, 2)`.

### Using `.T`

The simplest way to transpose a NumPy array is using `.T`.

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)