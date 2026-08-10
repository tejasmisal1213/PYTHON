# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)



# # factorial using Recursion
# def fact(n):
#     if (n == 0 or n== 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(6))

# # sum of n natural numbers using Recursion
# def sum(n):
#     if(n == 0):
#         return 0
#     else:
#         return n + sum(n-1)
#     print(sum(5))

# print all element in lit
def print_list(list,idx=0):

    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)
Ex = ["shweta", "Apeksha","Diksha","Mahi", "Sneha"]
print_list(Ex)