# NumPy Array Properties

- NumPy provides properties to 
  understand the structure, data type, and memory usage of an array.

## `ndim`

- `ndim` returns the number of 
   dimensions of an array.

- arr.ndim

## shape

- shape returns the size of the array 
  along each dimension.
- arr.shape
- - Example: (2, 3) means 2 rows and  
    3 columns.

## size

- size returns the total number of 
  elements in an array.
- arr.size
- For shape (2, 3): 2 × 3 = 6 

## dtype

- dtype represents the data type of 
 the array elements.
- arr.dtype

- Common NumPy data types include:
  int8, int32, int64
  loat32, float64 , bool

## itemsize

- itemsize returns the memory 
  occupied by one array element in bytes.
- itemsize depends on the array's 
  dtype.
- itemsize = dtype / 8 bytes.

## nbytes

- nbytes returns the total memory 
  occupied by all elements of an array in bytes.

- nbytes = size × itemsize