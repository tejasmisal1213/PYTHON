# Comparison Logical operations
import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# print(arr > 25)
# print(arr < 30)
# print(arr >= 30)
# print(arr == 30)
# print(arr != 30)

# Logical operations
arr = np.array([ 10,20,30,40,50])

print(np.logical_and(arr > 10 , arr < 25) )
print((arr > 10 ) & (arr < 25))

print(np.logical_or(arr < 10, arr > 20))
print((arr < 10 ) | ( arr > 20))

print(np.logical_not(arr > 15))
print( ~ ( arr > 15))
