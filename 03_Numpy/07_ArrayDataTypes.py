# Numpy Array datatypes
import numpy as np
arr = np.array([10, 20, 30])   # int8 ,int16 , int32 ,64int 64
arr = np.array([10.5, 20.5, 30.5]) # float16float32 ,float64
arr = np.array([True, False, True])  # bool

# astype()  --> convert dtype to other dtype 

arr = np.array([10, 20, 30])
print(arr.dtype)
float_arr = arr.astype(np.float32)

#1. Integer → Float
arr = np.array([10, 20, 30])
new_arr = arr.astype(np.float32)
print(new_arr)
print(new_arr.dtype)

# 2. Float → Integer
arr = np.array([10.9, 20.5, 30.2])
new_arr = arr.astype(np.int32)
print(new_arr)

# 3. Integer → Boolean      # 0 → False , non-0 → True , 
arr = np.array([0, 1, 5, -2])
new_arr = arr.astype(bool)
print(new_arr)

4. Boolean → Integer
arr = np.array([True, False, True])
new_arr = arr.astype(np.int32)
print(new_arr)

