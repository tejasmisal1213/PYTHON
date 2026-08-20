import numpy as np

# Creating numpy array 
arr = np.array([10,20,30])
print("Array:",arr)
print("Type", type(arr))

#indexing 
print("First Element" , arr[0])
print('Last Element' , arr[-1])

# Numpy basic operations

arr = np.array([10,20,30,40,50])
print("Array" ,arr)
print("Add" , arr + 5)
print("Sub" ,arr - 5)
print("Mul" ,arr * 2)
print("Div" ,arr / 2)

# Practice 1
import numpy as np
arr = np.array([5,10,15,20,25])
print("Array:" , arr)
print("First Ele:" , arr[0])
print("Last Ele: " , arr[-1])
print(arr * 3)
print(arr + 30)

#Practice 2
arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr[1][1]) # to print 5
print(arr[0]) # to print first row
print(arr[2]) # to print 3rd row

# Practice 3 
a = np.array([2,4,6])
print(a + 10)
print(a * 3)

arr = np.array([10, 20, 30])
print(type(arr[0] / 2))

arr = np.array(["Python" , " AI" ])
print(arr.dtype)

arr = np.array([10, 20, 30] , dtype =np.float32)
print(arr.dtype)
print(arr)

arr = np.array([10,20,30,40,50])
print(arr.ndim)  # no of diamenaion
 
arr = np.array([10,20,30,40,50])
print(arr.shape) # no of elements

arr = np.array([[1,2,3],
                [4,5,6]])
print(arr.shape)   # 2 --> rows , 3 --> coloumns

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr.size)    # no of elements

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# np.zeros
arr = np.zeros(5) # by default float zeros 
print(arr)
arr = np.zeros(2 , dtype = int) # int zeros user defined
print(arr)

# 2D zeros
arr = np.zeros((2,4))   # 2 rows , 4 coloumn
print(arr)
