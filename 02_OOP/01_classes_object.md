## What is a Class?

- A class is a blueprint or template used to create objects.

 
class Student:
    name = "Tejas"
    age = 22
 

## What is an Object?

- An object is an instance of a class.
 
student1 = Student()
 
## Constructor in Python
 - A constructor is a special method that is automatically called when an object is created.
  - __init__()

## Attributes

- Attributes are variables that store data related to an object.

 
class Student:
    name = "Tejas"
    age = 22

## Instance Method

- An instance method works with the object and uses `self`.

- def study(self):
 
 ## Static Method

A static method does not depend on the object or class data.

- It is defined using the `@staticmethod` decorator.

- @staticmethod
  def add(a, b):
 
 
