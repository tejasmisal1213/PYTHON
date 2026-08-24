# NumPy Slicing

- Slicing is used to access a portion of a NumPy array.
- Unlike indexing, which usually accesses a specific element, slicing can access multiple elements.

## Basic Slicing

- The basic slicing syntax is:

    arr[start:stop:step]

- `start` specifies where slicing begins.
- `stop` specifies where slicing ends.
- `step` specifies the interval between elements.
- The `stop` index is not included.

## General Slicing Pattern

- 1D:

    arr[start:stop:step]

- 2D:

    arr[row_start:row_stop:row_step, column_start:column_stop:column_step]

- 3D:

    arr[block_slice, row_slice, column_slice]
 
## Important Rules

- Start index is included.
- Stop index is excluded.
- `:` means all elements along that dimension.
- A positive step moves forward.
- A negative step moves backward.
- `[::-1]` reverses an array along that dimension.

 