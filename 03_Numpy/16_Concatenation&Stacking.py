# Concatenate
import numpy as np
# arr1= np.array([1,2,3])
# arr2= np.array([4,5,6])
# res= np.concatenate((arr1,arr2))
# print(res)

#2D array concate
# arr1 = np.array([
#     [1, 2],
#     [3, 4]])
# arr2 = np.array([
#     [5, 6],
#     [7, 8]])
# res = np.concatenate((arr1,arr2), axis=0) #Rows added 
# print("#Rows added \n", res)
# res2=np.concatenate((arr1,arr2), axis=1)
# print("#coloumn Added \n",res2)

#Vertical stack
# arr1 = np.array([
#     [1, 2],
#     [3, 4]])
# arr2 = np.array([
#     [5, 6],
#     [7, 8]])
# print("#rows added\n",np.vstack((arr1,arr2)))
# print("#Column added\n", np.hstack((arr1,arr2)))

#Stack
# arr1= np.array([1,2,3]) #shape (3,0)
# arr2=np.array([4,5,6])  #shape (3,0)
# print(np.stack((arr1,arr2))) #shape (2,3)