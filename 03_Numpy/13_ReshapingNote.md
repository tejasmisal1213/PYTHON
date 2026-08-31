# NumPy Reshaping

### reshape()

- `reshape()` changes the shape of an 
  array without changing its elements.
- The total number of elements must  
remain the same.

    arr.reshape(2, 3)

### Shape and Element Count

- The new shape must have the same 
  total number of elements as the original array.

    2 × 3 = 6

- Invalid shapes raise an error when 
  the element count does not match.

### -1 in reshape()

- `-1` allows NumPy to automatically 
  calculate one dimension.

    arr.reshape(2, -1)

- Only one dimension can be specified 
  as `-1`.

### Multi-dimensional Reshaping

- Arrays can be reshaped into 2D, 3D, 
  or higher-dimensional structures as long as the element count remains the same.

    arr.reshape(2, 3, 4)

### reshape(-1)

- `reshape(-1)` can convert an array 
  into a one-dimensional structure.

### reshape() vs resize()

- `reshape()` requires the total 
  number of elements to remain the same.
- `resize()` can change the size of 
   the original array.

 