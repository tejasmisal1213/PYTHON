# NumPy Arithmetic Operations

- NumPy supports arithmetic operations directly on arrays.
- Operations are generally performed element-wise.

### Basic Arithmetic

- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division
- `//` → Floor Division
- `%` → Modulus
- `**` → Power

### Scalar Operations

- A scalar operation applies one value to every element of an array.

    arr + 5
    arr * 2

### Array-to-Array Operations

- Two arrays of compatible shapes can be operated element-wise.

    a + b
    a - b
    a * b
    a / b

### In-Place Operations

- Operators such as `+=`, `-=`, `*=`, and `/=` can modify the existing array.

    arr += 5

### NumPy Arithmetic Functions

- NumPy also provides functions for arithmetic operations.

    np.add()
    np.subtract()
    np.multiply()
    np.divide()

### Element-wise vs Matrix Multiplication

- `*` performs element-wise multiplication.

    a * b

- `@` performs matrix multiplication.

    a @ b

- `np.matmul()` can also be used for matrix multiplication.

 