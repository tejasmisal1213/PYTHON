# Array Bacis

#  array from Diff data

import numpy as np 
arr = np.array([10,20,30,40])
print(arr)

 
arr = np.array([5.5,10.5,15.5,20.5])
print(arr)

arr = np.array([True,False,True,False])
print(arr)

""" 1D Array """
arr = np.array([5,10,15,20])
print(arr)

""" 2D Array """"
arr = np.array([[1,2,3,4],
                [5,6,7,8] ] )
print(arr)

''' 3D Array '''

arr = np.array([
    [ 
        [1,2],
        [3,4]
    ] , 
    [ [5,6],
      [7,8]
    ]
])
print(arr.shape)
print(arr.ndim)
print(arr.size)

""" Empty() """

arr = np.empty(5)
 
arr[:] = 5
print(arr)

arr = np.empty((2,3))
print(arr)
print(arr.shape)
print(arr.ndim)

""" full() """"
arr = np.full(5,"T")
print(arr)

arr = np.full((2,3),"S")
print(arr)

""" arrange() """"

arr = np.arange(1,6) #start 1 , End 6 (not include)
print(arr)

arr = np.arange(0,10,2)
print(arr)

arr1 = np.arange(10,0,-2)  # Reverse Sequence
print(arr1)

""" Linspace() """"

arr = np.linspace(0,10,2) # start , stop , num
print(arr)

