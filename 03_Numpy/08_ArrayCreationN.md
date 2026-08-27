# NumPy Array Creation

- NumPy provides several functions to 
  create arrays efficiently.

### np.zeros()

- Creates an array filled with zeros.

    np.zeros(5)

- Shape can also be specified.

    np.zeros((2, 3))

### np.ones()

- Creates an array filled with ones.

    np.ones(5)

### np.full()

- Creates an array filled with a specified value.

    np.full((2, 3), 7)

### np.empty()

- Creates an array without initializing its values.
- The values may contain existing memory data.

    np.empty((2, 2))

### np.arange()

- Creates a sequence of numbers using a start, stop, and step.

    np.arange(0, 10, 2)

- The stop value is excluded.

### np.linspace()

- Creates a specified number of equally spaced values between a start and stop value.

    np.linspace(0, 10, 5)

- Unlike `arange()`, it specifies the number of values instead of the step.

### np.eye()

- Creates an identity matrix.

    np.eye(3)

### np.diag()

- Creates a matrix with specified values on the main diagonal.

    np.diag([10, 20, 30])

### *_like() Functions

- `np.zeros_like()` creates zeros with the same shape as an existing array.
- `np.ones_like()` creates ones with the same shape.
- `np.full_like()` creates an array with the same shape and a specified value.

