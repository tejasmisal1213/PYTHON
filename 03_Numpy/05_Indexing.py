# import numpy as np

#1D array Inedexing  """ arr[index] """
# arr = np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[1])
# print(arr[-0])

#2D array Inedexing  """ arr[rows , column] """
# arr = np.array([
#     [10,20,30],
#     [40,50,60]] )
# print(arr[0,0])     #10
# print(arr[-1,-1])   #60
# print(arr[-2,-3])   #10

#3D array Inedexing
# arr = np.array([
#     [ 
#         [1,2],
#         [3,4] 
#     ] ,
#     [   [5,6],
#         [7,8]
#     ] ] )

# print(arr[-1,1,-2])

# Row & Column Indexing
# arr = np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]])
# print(arr[0])      # complete row of 0 index
# print(arr[ :,0])   # : --> all rows , 0 index --> first column
# print(arr[0,:])       #0 index --> row , : --> all column

# 3D indexing -- complete Blocks , Rows and Columns
# arr = np.array([
#     [ [1,2],
#       [3,4]],
#     [ [5,6],
#       [7,8]]])
# print(arr.shape)   """arr[block, row, column]"""
# print([0])   # complete 1st 2D block 
# print([1])   # complete 2nd 2d block

# print([0,1]) #complete [] row from [] block 

