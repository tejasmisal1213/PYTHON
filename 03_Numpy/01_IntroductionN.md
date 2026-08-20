# NumPy Introduction

- NumPy stands for **Numerical Python*.

- NumPy is a Python library used for **numerical computing and data processing*.

- NumPy is widely used in **AI, Machine Learning, Data Science, and Scientific Computing*.

## Importing NumPy

- NumPy can be imported using the `import` statement.


import numpy as np


- `np` is the commonly used **alias* for NumPy.

## NumPy Array

- NumPy provides a powerful data structure called **ndarray*.

- `ndarray` stands for **N-dimensional array*.

### Creating an Array
 
arr = np.array([10, 20, 30, 40, 50])
 

- `np.array()` is used to create a NumPy array.

## Python List vs NumPy Array

- Python Lists are general-purpose data structures.

- NumPy Arrays are optimized for **numerical operations*.

- NumPy performs mathematical operations **element-wise*.
 
arr = np.array([10, 20, 30])
print(arr * 2)
 

## Array Indexing

- NumPy arrays use **zero-based indexing*, similar to Python Lists.

```python
arr[0]    # First element
arr[-1]   # Last element
```

## Array Arithmetic Operations

- NumPy allows mathematical operations directly on arrays.

```python
arr + 5
arr - 5
arr * 2
arr / 2
```

- Operations are performed **element-wise*.

## Data Type (`dtype`)

- `dtype` represents the **data type of elements* stored in a NumPy array.

```python
arr.dtype
```

- Common NumPy data types include:

`int64` → Integer

`float64` → Floating-point number

`float32` → 32-bit floating-point number

- `float64` uses **64 bits (8 bytes)** to store a floating-point value.

## Array Properties

- `ndim` → Number of dimensions
- `shape` → Size of each dimension
- `size` → Total number of elements
- `dtype` → Data type of elements

 
## Array Creation Functions

### `np.zeros()`

- Creates an array filled with **0**.
 
### `np.ones()`

- Creates an array filled with **1**.
 - By default, `np.zeros()` and `np.ones()` create arrays with `float64` dtype.
