# class Student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
     

# s1= Student("Tejas", 90)
# print(s1.name)
# print(s1.marks)


#Getter and Setter 
class Student:
    def __init__(self,marks):
        self.__marks = marks

    def get_marks(self):   # Getter
        return self.__marks

    def set_marks(self,marks): # Setter
        self.__marks = marks

s1 = Student(80)
print(s1.get_marks())

s1.set_marks(90)
print(s1.get_marks())

