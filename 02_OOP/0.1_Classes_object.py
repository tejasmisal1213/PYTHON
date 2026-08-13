# class Student:
#     name ="Tejas"
# s1 =Student()
# print(s1.name)

class Student:
    def __init__(self ,name):
        self.name = name
        print("Adiing new Ai Er in company...")
s1 = Student("Tejas")
print(s1.name)