# NumPy Array Basics

- NumPy arrays are used to store and process numerical data efficiently.

## Creating NumPy Arrays

- `np.array()` is used to create a NumPy array.

- Arrays can be **1D, 2D, or 3D** depending on their structure.

## 1D Array

- A one-dimensional array contains elements in a single sequence.

## 2D Array

- A two-dimensional array contains **rows and columns**.
 
## 3D Array
- A three-dimensional array contains multiple 2D arrays.


## Array Creation Functions

### `np.zeros()`

- Creates an array filled with `0`.

### `np.ones()`

- Creates an array filled with `1`.

### `np.empty()`

- Creates an array without initializing its elements to a specific value.

- The initial values are not guaranteed to be `0`.

### `np.full()`

- Creates an array filled with a specified value.

### `np.arange()`

- Creates values within a range using a specified step.
- The `stop` value is not included.
 
 
### `np.linspace()`

- Creates a specified number of evenly spaced values between two limits.
 
## `arange()` vs `linspace()`

- `arange()` → controls the **step size**.
- `linspace()` → controls the **number of values**.

## Basic Array Properties

- `ndim` → Number of dimensions
- `shape` → Size of each dimension
- `size` → Total number of elements
- `dtype` → Data type of elements
