# NumPy Concatenation and Stacking

### Concatenation

- Concatenation means joining two or 
  more NumPy arrays along an existing axis.

- The main function used is `np.concatenate()`.

### np.concatenate()

- Joins arrays along an existing axis.
- `axis=0` joins arrays vertically and increases rows.
- `axis=1` joins arrays horizontally and increases columns.
- Arrays must have compatible dimensions along the other axes.

### axis=0

- Joins arrays vertically.
- Rows increase.
- For 2D arrays, the number of columns remains the same.

### axis=1

- Joins arrays horizontally.
- Columns increase.
- For 2D arrays, the number of rows remains the same.

### np.vstack()

- `vstack()` means vertical stacking.
- Joins arrays from top to bottom.
- Increases the number of rows.
- Similar to concatenation along `axis=0`.

### np.hstack()

- `hstack()` means horizontal stacking.
- Joins arrays from left to right.
- Increases the number of columns.
- For 2D arrays, it behaves similarly to concatenation along `axis=1`.

### np.stack()

- `stack()` combines arrays by creating a new axis.
- Unlike `concatenate()`, it increases the number of dimensions.
- The arrays being stacked generally need to have the same shape.
- The `axis` parameter determines the position of the new axis.

### concatenate() vs stack()

- `concatenate()` → joins along an existing axis.
- `stack()` → creates a new axis and joins arrays along it.

### concatenate() vs vstack() vs hstack()

- `concatenate(axis=0)` → vertical joining.
- `concatenate(axis=1)` → horizontal joining.
- `vstack()` → vertical joining.
- `hstack()` → horizontal joining.
- `stack()` → creates a new dimension.

### Shape Changes

For two 2D arrays with shape `(2, 2)`:

- `concatenate(axis=0)` → `(4, 2)`
- `concatenate(axis=1)` → `(2, 4)`
- `vstack()` → `(4, 2)`
- `hstack()` → `(2, 4)`

For two 1D arrays with shape `(3,)`:

- `concatenate()` → `(6,)`
- `stack()` → `(2, 3)` when using the default axis

### Key Points

- Concatenation joins arrays along an existing axis.
- `axis=0` generally increases rows.
- `axis=1` generally increases columns.
- `vstack()` performs vertical stacking.
- `hstack()` performs horizontal stacking.
- `stack()` creates a new axis.
- `concatenate()` and `stack()` are different operations.
- Understanding shape and axis is essential when combining NumPy arrays.
 