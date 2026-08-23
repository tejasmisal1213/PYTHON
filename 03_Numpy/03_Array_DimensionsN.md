**# NumPy Array Dimensions**

- Array dimension represents the number of axes in a NumPy array.

## ndim

- `ndim` returns the number of dimensions of an array.

## 0D Array

- A 0D array contains a single value.

## 1D Array

- A 1D array contains elements in a single sequence.

## 2D Array

- A 2D array contains rows and columns.

## 3D Array

- A 3D array contains multiple 2D arrays.

- arr = np.zeros((2, 2, 2))

- Shape (2, 2, 2) means 2 blocks, 2 rows, and 2 columns.

- Total elements can be calculated by multiplying all dimensions.
2 × 2 × 2 = 8

## 4D Array

- A 4D array contains data across four dimensions.
- arr = np.zeros((2, 3, 4, 5))

## Shape and Dimensions

- ndim → Number of dimensions
- shape → Size along each dimension
- size → Total number of elements

## Axes

- An axis represents a specific dimension of a NumPy array.
- The number of axes is equal to the number of dimensions (`ndim`).

### Axes in a 2D Array

- A 2D array has two axes:

`axis=0` → operates down the rows

`axis=1` → operates across the columns

Example:

 
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(arr, axis=0))

### Axes in a 3D Array

- A 3D array has three axes: axis=0, axis=1, and axis=2.

- (A, B, C)
- axis=0 → (B, C)
- axis=1 → (A, C)
- axis=2 → (A, B)