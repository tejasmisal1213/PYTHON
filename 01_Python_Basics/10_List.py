# List in Python
student = ["Tejas", 21 , "Beed"]
print(student)
print(student[0])


# List slicing
marks = [10, 20, 30, 40, 50]
print(marks[1:4])
print(marks[:3])
print(marks[2:5])
print(marks[::2]) # gap of 2
print(marks[::-1]) # reverse the list

# List methods
cars = ["BMW","Defender", "Mercedes"]
print(cars)
print(len(cars)) # length of the list
cars.append("RR") # add element at the end
print(cars)
cars.insert(1, "Audi") # add element at specific index
print(cars) 
cars.sort() # sort the list
print(cars)
cars.reverse() # reverse the list
print(cars)
cars.sort(reverse=True) # sort the list in descending order
print(cars)
cars.remove("Audi") # remove element from the list
print(cars)
cars.pop() # remove last element from the list
print(cars)
cars.pop(1) # remove element at specific index

