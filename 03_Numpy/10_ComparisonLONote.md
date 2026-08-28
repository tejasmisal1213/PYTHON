# NumPy Comparison and Logical Operations

### Comparison Operators

- NumPy performs comparisons 
  element-wise and returns a Boolean array.

- `>` → Greater than
- `<` → Less than
- `>=` → Greater than or equal to
- `<=` → Less than or equal to
- `==` → Equal to
- `!=` → Not equal to

### Boolean Array

- Comparison operations return `True` 
  or `False` for each element.

-   arr > 25

### Logical Functions

- `np.logical_and()` → Both 
   conditions must be True.
- `np.logical_or()` → At least one 
   condition must be True.
- `np.logical_not()` → Reverses True 
   and False.

### Logical Operators

- `&` → AND
- `|` → OR
- `~` → NOT

- Parentheses should be used when 
 combining NumPy conditions.

-  (arr > 10) & (arr < 50)

 