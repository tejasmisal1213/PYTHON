# NumPy Array Data Types

- NumPy arrays have a fixed data type represented by `dtype`.

## Integer --> #int8,int16,int32 64int
## Float   --> float16,float32,loat64
## Boolean --> True , False

## Specifying dtype

- We can specify the required data type while creating an array.

    arr = np.array([10, 20, 30], dtype=np.float32)

- `float32` stores the values as 32-bit floating-point numbers.

## astype()

- `astype()` is used to convert an array from one data type to another.

    arr = np.array([10, 20, 30])

    new_arr = arr.astype(np.float32)

- Integer values are converted to floating-point values.

## Float to Integer

    arr = np.array([10.5, 20.8, 30.2])

    new_arr = arr.astype(np.int32)

- The decimal part is removed during conversion.

## Boolean Conversion

- `0` converts to `False`.
- Non-zero values convert to `True`.

    arr = np.array([0, 1, 5, -2])

    print(arr.astype(bool))

## Important

- `astype()` creates a converted array.
- Converting between data types can cause data loss.
- Data type conversion is useful when preparing numerical data for AI/ML workflows.