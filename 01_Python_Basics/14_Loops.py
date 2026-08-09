# # 1 to 100 numbers using while loop
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# # 100 to 1 numbers using while loop
# a = 100
# while a >= 1:
#     print(a)
#     a -= 1 

# mul table of n number
# n = int(input("Enter a number to print its multiplication table: "))
# m = 1
# while m <= 10:
#     print(n*m)
#     m += 1

# traversign list using while loop
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# search for an item x in list using while loop
# num = [1,4,9,16,25,36,49,64,81,100]
# x = 81
# i = 0
# while i < len(num):
#     if num[i] == x:
#         print("found at indx " , i)
#     else:
#         print("Finding")
#     i += 1


# skipping numbers in while loop 
# i = 0
# while i <= 10:
#     if(i == 5):
#         i += 1
#         continue

#     print(i)

    # i += 1


# print odd numbers using while loop
# i = 0
# while i <= 10:
#     if(i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# n = 1 # print sum of first n numbers using while loop
# sum = 0
# while n <= 5:
#     sum += n
#     n += 1
# print(sum)




# For Loop 
# for i in range(5):
#     print(i)




# range fun

# for i in range(10):  #range(stop)
#     print(i)

# for i in range(1,10): # range(start,stop)
#     print(i)

# for i in range(0,10,2): # range(start,stop,stepsize)
#     print(i)

# for i in range(1,10): # printing 1 to 10
#     print(i)

# for i in range(11,0,-1): #printing 10 to 1
#     print(i) 


# n = 5  #sum of first n numbers using for loop
# sum = 0
# for i in range(1 , n+1):
#     sum +=i
# print("Sum of first ", n , " numbers is: ", sum)


# n = int(input("Enter a number to print fact: "))  # factorial of n
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("Factorial of ", n , " is: ", fact)