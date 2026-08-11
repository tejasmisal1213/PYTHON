# File Input and Output in Python

## What is File Handling?

File handling is used to create, read, write, and modify files using Python.

## Opening a File

```python
file = open("example.txt", "r")
```
## File Modes

- r --> Read an existing file
- w --> Write to a file
- a --> Append data to a file
- x --> Create a new file

## Writing to a File

```python
file = open("example.txt", "w")
file.write("Hello, Python!")
file.close()
```

## Reading a File

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

## Important Functions and Methods

- open() --> Opens a file
- read() --> Reads the file
- readline() --> Reads one line
- readlines() --> Reads all lines as a list
- write() --> Writes data to a file
- close() --> Closes the file

## Important Points

- Use `r` to read a file.
- Use `w` to write or overwrite a file.
- Use `a` to add content to an existing file.
- The `with` statement is recommended because it automatically closes the file.