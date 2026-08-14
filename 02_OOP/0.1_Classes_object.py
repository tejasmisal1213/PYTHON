# class Student:
#     name ="Tejas"
# s1 =Student()
# print(s1.name)

# class Student:
#     def __init__(self ,name):
#         self.name = name
#         print("Adiing new Ai Er in company...")
# s1 = Student("Tejas")
# print(s1.name)

class Student:
    def __init__(self , name,marks):
        self.name = name
        self.marks = marks 
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Hi", self.name , "Your avg score is:", sum/3)
s1 = Student("Tony Stark", [99,99,99])
s1.get_avg()