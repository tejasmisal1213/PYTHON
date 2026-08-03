# What is a Data Type?

A data type specifies the type of value a variable can store.

1. Integer (int)

An integer is a whole number without a decimal point.

Examples
age = 21
 
Stores whole numbers
Can be positive, negative, or zero
No decimal point

2. Float (float)
   A float is a number that contains a decimal point.

Examples
price = 99.99

Stores decimal values
Can be positive or negative
Used for precise numerical calculations

3. Boolean (bool)
  A boolean data type stores only two values: True or False.

Examples
is_student = True
 
Used in decision making
Commonly used with conditions and loops
Values are case-sensitive: True and False

4. String (str)
  A string is a collection of characters enclosed in quotes.

Examples
name = "Tejas"
city = 'Pune'

Stores text data
Can use single or double quotes
Supports indexing and slicing

5. None (NoneType)
   None represents the absence of a value.

Examples
result = None
data = None
 
Used when a variable has no value assigned.
Represents null or empty value.
Python keyword: None

## Checking Data Types
Use the type() function to check the data type of a variable.

Example
age = 21
print(type(age))

price = 99.99
print(type(price))

name = "Tejas"
print(type(name))
Output
<class 'int'>
<class 'float'>
<class 'str'>