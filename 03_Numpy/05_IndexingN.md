# NumPy Indexing

- Indexing means accessing a specific element or portion of a NumPy array using its position.


## General Indexing Pattern

- 1D array:

    arr[index]

- 2D array:

    arr[row, column]

- 3D array:

    arr[block, row, column]

## 1D Array Indexing

- 1D array indexing uses a single index.
 
- NumPy indexing starts from `0`.

    Value:  10  20  30  40  50
    Index:   0   1   2   3   4

## Negative Indexing

- Negative indexing starts from the end of the array.

- `-1` represents the last element.

    Value:   10   20   30   40   50
    Index:    0    1    2    3    4
             -5   -4   -3   -2   -1

## 2D Array Indexing

- A 2D array uses row and column indexing.
 
- Syntax:

    arr[row, column]

## Complete Row Access

- A complete row can be accessed using:

    arr[row, :]

 

- `:` means all elements along that dimension.

    

## Complete Column Access

- A complete column can be accessed using:

    arr[:, column]

- `arr[:, 0]` means all rows and column `0`.
 
## 3D Array Indexing

- A 3D array uses block, row, and column indexing.

- Shape:

    (2, 2, 2)

- Syntax:

    arr[block, row, column]

## Complete Block Access

- `arr[0]` accesses the first 2D block.


## Complete Row Access in 3D

    print(arr[0, 1])

Output:

    [3 4]

- `0` → first block
- `1` → second row

## Complete Column Access in 3D

    print(arr[:, :, 0])

Output:

    [[1 3]
     [5 7]]

- First `:` → all blocks
- Second `:` → all rows
- `0` → first column

    print(arr[:, :, 1])

Output:

    [[2 4]
     [6 8]]


 

 