# NumPy Flatten and Ravel

### flatten()

- `flatten()` converts a 
  multi-dimensional array into a one-dimensional array.
- `flatten()` always returns a copy of 
  the original array.

    arr.flatten()
 
### ravel()

- `ravel()` also converts an array 
  into a one-dimensional array.
- `ravel()` returns a view when 
  possible, so changes may affect the original array.

    arr.ravel()

### reshape(-1)

- `reshape(-1)` can also convert an 
  array into a one-dimensional structure.

    arr.reshape(-1)

### flatten() vs ravel()

- `flatten()` → returns a copy
- `ravel()` → returns a view when 
  possible
- `reshape(-1)` → reshapes into 1D and 
  may return a view when possible

### Copy vs View

- A copy has its own separate data.
- A view shares data with the original 
 array.
- Changing a view can change the 
 original array.
 