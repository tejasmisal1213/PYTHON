# Slicing --> Index arr[start:stop:step]
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[0:5])
# print(arr[2:3])
# print(arr[:]) 

# #Negative 
# print(arr[::-1]) # reversed array

# # Slicing 2D arrays --> arr[row_slice, column_slice]
# """ arr[row_start:row_stop:row_step,
#     col_start:col_stop:col_step] """

# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])
# print(arr.shape)
# print(arr[0:2, :])   #0:2 → rows 0 and 1 , : → all columns


# 3D array slicing --> arr[block, row, column]
""" arr[block_slice, row_slice, column_slice] """

# arr = np.array([
#     [[1, 2, 3],
#      [4, 5, 6]],

#     [[7, 8, 9],
#      [10, 11, 12]]
# ])
# print(arr[1:, :, :2])
# print(arr[:, 1:, :])
# print(arr[:, :, 1:])
# print(arr[:, :, ::2])