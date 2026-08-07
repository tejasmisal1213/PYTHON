# Simple Dict 
student = { "name" : "Tejas",
        "Age" :  21 , "City" : "Pune"}
print(student)

#Accesing Items or value from dict
print(student["name"])
print(student["Age"])

# Add new key in dict
student["Subject"]= "Python"
student.update({"College":"JSPM"})
print(student)

# Dict Methods
print(student.keys()) # Print all keys  
print(student.values()) # Print all values
print(student.items()) # Print all key-value pairs as tuples
print(student.get("name")) # Get value of key.... # no Error if key not found 



