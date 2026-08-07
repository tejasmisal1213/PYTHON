numbers = {1,2,3,4,5}
print(numbers)
print(len(numbers())) # length of the set

print(numbers.pop()) # remove random element from set
print(numbers.clear()) # remove all elements from set

numbers.add(6) # add element in set
numbers.remove(3) # remove element from set
print(numbers)

# Set methods
number = {4,5,6,7,8}

print(numbers.union(number)) # union of two sets
print(numbers.intersection(number)) # intersection of two sets
