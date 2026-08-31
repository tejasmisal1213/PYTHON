#Reshaping --> changes shape but total number of elements should same 
# import numpy as np 
# arr = np.array([1,2,3,4,5,6])  #total 6 elements 
# print(arr.reshape(2,3))    # 2*3 = 6 elemnets
# print(arr.reshape(2, 3))   
# print(arr.reshape(3, 2))
# print(arr.reshape(1, 6))
# print(arr.reshape(6, 1))

# -1 in reshape  --> only 1 diamension can be -1 
# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr.reshape(-1,2))  # Assume -1 as 3 
# print(arr.reshape(2,-1))

# reshape with 2D existing array
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr.reshape(3, 2))


#3D array reshape
# arr = np.arange(8)
# print(arr.reshape(2, 2, 2))


#resize()   --> chnage the size of array
# arr = np.arange(6) 
# arr.resize(2, 2)
# print(arr)

#Flattering --> cinverting multi D array to 1D
# arr = np.array([
#      [1, 2, 3],
#      [4, 5, 6] ])
# print(arr.reshape(-1))