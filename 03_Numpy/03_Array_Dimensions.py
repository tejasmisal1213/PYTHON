# Array Diamensions
# 0D array
arr = np.array(10)  # 0D because only scalar value.
print(arr)
print(arr.ndim)

# 1D array
arr = np.array([10,20,30,40])  # 1D array / Vecotr
print(arr)
print(arr.ndim) 

# 3D array
arr = np.array([
    [
    [1,2],
    [3,4] 
    ],
    [ [5,6],
      [7,8]
    ] ] )
print(arr.ndim) # 3D 
print(arr.shape) #2 block , 2 rows , 2 clm 

# 4D array
arr = np.zeros((3,2,4,5))
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)



# 3D axes
import numpy as np 
arr = np.array([
    [[1,2,],
     [3,4]],
    [[5,6],
     [7,8]]
    ])
# print(arr)
# print(arr.shape)
# print(arr.ndim)

print(np.sum(arr , axis = 0))   # Matrix 1          Matrix 2
print(np.sum(arr , axis = 1))   #  1  2              5  6 
print(np.sum(arr , axis = 2))   #  3  4              7  8