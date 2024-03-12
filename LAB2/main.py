# -*- coding: utf-8 -*-
"""Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12V1Ndznj0M65EmiKLYNl9VyHnRsJpcJa

Warning:

After each exercise from now on, do a git commit and write in a message what you did.

3.
Write a Python program that takes input from the user to create a list of integers and then performs the following operations:

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers.
  
  c. Sorting: Sort the list in ascending order.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Sorted list: [1, 2, 5, 8, 9]
  ```
"""

# # Input
# input_numbers = input("Enter a series of space-separated integers: ")
#
# # Convert Input:
# numbers_list = [eval(i) for i in input_numbers.split(" ")]
#
# # Sorting:
# numbers_list = sorted(numbers_list)
#
# # Print Output
# print("Sorted list:", numbers_list)

"""-----------------------------------------------------------------------------

Difference between Lists and Tuples:

Lists are mutable, meaning their elements can be changed after creation, while tuples are immutable, meaning their elements cannot be changed after creation.
Lists are represented by square brackets [ ], whereas tuples are represented by parentheses ( ).
Lists have methods like append(), insert(), and remove() to modify the list, while tuples do not support such methods due to their immutability.
Lists are typically used when the elements need to be modified or updated frequently, while tuples are used when the data is meant to be constant or unchangeable.

-----------------------------------------------------------------------------

4.
Extend the previous Python program to include tuples. Now, in addition to creating a list of integers from user input, the program should also create a tuple of those integers and perform the following operations:

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers and a tuple of integers.

  c. Sorting: Sort both the list and the tuple in ascending order.

  d. Print Output: Print the sorted list and tuple.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9
  
  Sorted list: [1, 2, 5, 8, 9]
  Sorted tuple: (1, 2, 5, 8, 9)
  ```
"""

# # Input
# input_numbers = input("Enter a series of space-separated integers: ")
#
# # Convert Input:
# numbers_list = [eval(i) for i in input_numbers.split(" ")]
# sorted_tuple = tuple(numbers_list)
#
# # Sorting:
# numbers_list = sorted(numbers_list)
# sorted_tuple = sorted(sorted_tuple)
#
# # Print Output
# print("Sorted list:", numbers_list)
# print("Sorted tuple:", sorted_tuple)

"""5.
Extend the previous Python program to demonstrate the manipulation of lists using the append(), insert(), and remove() functions, and to emphasize the immutability of tuples.

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers and a tuple of integers.
  
  c. Manipulate List: Use the append(), insert(), and remove() functions to modify the list.
  
  d. Attempt to Modify Tuple: Try to modify the tuple using the same operations as the list.
  
  e. Print Output: Print the modified list and attempt to print the modified tuple.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Modified list: [5, 2, 20, 1, 9, 10]
  Tuple remains unchanged: (5, 2, 8, 1, 9)
  ```
"""

# # Input
# input_numbers = input("Enter a series of space-separated integers: ")
#
# # Convert Input
# numbers_list = [eval(i) for i in input_numbers.split(" ")]
# numbers_tuple = tuple(numbers_list)
#
# # Manipulate List
# numbers_list.append(10)
# numbers_list.insert(2, 20)
# del numbers_list[0]
#
# # Attempt to Modify Tuple (this will raise an error)
# try:
#     numbers_tuple.append(10)
# except AttributeError:
#     print("Tuples are immutable and cannot be modified.")
# try:
#     numbers_tuple.insert(2, 20)
# except AttributeError:
#     pass  # Insert operation will also raise an error
# try:
#     del numbers_tuple[0]
# except TypeError:
#     pass  # Remove operation will also raise an error
#
# # Print Output
# print("Modified list:", numbers_list)
# print("Tuple remains unchanged:", numbers_tuple)

"""--------------------------------------------------------------------------------
1. **Set**:
A set in Python is a collection of unique elements that are unordered. This means that you cannot access elements by indices, and the elements are stored in an unordered manner. The main feature of a set is that each element in the set must be unique. Sets are useful when you want to perform set operations, such as mathematical set operations (e.g., union, difference, intersection).

Example of creating a set:
```python
set = {1, 2, 3, 4, 5}  # Creating a set
print(set)  # Displaying the set
```

2. **Dictionary**:
A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are unique in the sense that they allow us to associate specific values with specific keys, making it easy to retrieve values by referring to their corresponding keys. Dictionaries are very useful when you want to store data in the form of key-value pairs, such as dictionary definitions, test scores, survey results, etc.

Example of creating a dictionary:
```python
dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}  # Creating a dictionary
print(dictionary)  # Displaying the dictionary
```
It's important to remember that both in sets and dictionaries, keys (in the case of dictionaries) and elements (in the case of sets) must be hashable, meaning they must be immutable (e.g., numbers, strings, tuples), and they must have a defined hashing method.

--------------------------------------------------------------------------------

6.
Additionally, introduce sets and dictionaries and perform basic operations on them.

  a. ...

  b. ...

  c. ...

  d. ...

  e. Set Operations: Perform union, intersection, and difference operations on the set.

  f. Dictionary Operations: Print the dictionary, add a new key-value pair, and delete an existing key-value pair.

  g. Print Output: Print the modified list, unchanged tuple, set operations results, and updated dictionary.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Original Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  Modified list: [5, 2, 20, 1, 9, 10]
  Tuple remains unchanged: (5, 2, 8, 1, 9)
  Union of set: {1, 2, 5, 9, 10, 11, 12}
  Intersection of set: {8, 5}
  Difference of set: {9}
  Updated Dictionary: {5: 25, 2: 4, 1: 1, 9: 81, 11: 121}

  ```
"""

# # Input
# input_numbers = input("Enter a series of space-separated integers: ")
#
# # Convert Input
# numbers_list = [eval(i) for i in input_numbers.split(" ")]
# numbers_tuple = tuple(numbers_list)
# numbers_set = set(numbers_tuple)
# numbers_dict = {}
#
# for index, element in enumerate(numbers_tuple):
#     numbers_dict[index] = element
#
# # Manipulate List
# numbers_list.append(10)
# numbers_list.insert(2, 20)
# numbers_list.remove(8)
#
# # Attempt to Modify Tuple (this will raise an error)
# try:
#     numbers_tuple.append(10)
# except AttributeError:
#     print("Tuples are immutable and cannot be modified.")
#
# # Set Operations
# set_union = numbers_set.union({2, 3, 8})
# set_intersection = numbers_set.intersection({2, 3, 8})
# set_difference = numbers_set.difference({2, 3, 8})
#
# # Dictionary Operations
# print("Original Dictionary:", numbers_dict)
# numbers_dict[10] = 8888
# del numbers_dict[0]
#
# # Print Output
# print("Modified list:", numbers_list)
# print("Tuple remains unchanged:", numbers_tuple)
# print("Union of set:", set_union)
# print("Intersection of set:", set_intersection)
# print("Difference of set:", set_difference)
# print("Updated Dictionary:", numbers_dict)

"""7. **Built-in Types and Type Conversion**

  Extend the previous Python program to demonstrate the use of built-in types and type conversion. Perform the following operations:

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. Type Conversion: Convert the list to a tuple, set, and dictionary. Convert the tuple to a list, set, and dictionary. Convert the set to a list, tuple, and dictionary. Convert the dictionary to a list, tuple, and set.

  h. Print Output: Print the results of the type conversion operations.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Original Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  List to Tuple: (5, 2, 20, 1, 9, 10)
  List to Set: {1, 2, 5, 9, 10, 20}
  List to Dictionary: {5: 25, 2: 4, 20: 400, 1: 1, 9: 81, 10: 100}
  Tuple to List: [5, 2, 8, 1, 9]
  Tuple to Set: {1, 2, 5, 8, 9}
  Tuple to Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  Set to List: [1, 2, 5, 9, 10, 20]
  Set to Tuple: (1, 2, 5, 9, 10, 20)
  Set to Dictionary: {1: 1, 2: 4, 5: 25, 9: 81, 10: 100, 20: 400}
  Dictionary to List: [5, 2, 20, 1, 9, 10, 11]
  Dictionary to Tuple: (5, 2, 20, 1, 9, 10, 11)
  Dictionary to Set: {1, 2, 5, 9, 10, 11, 20}
```
"""

# # Input
# input_numbers = input("Enter a series of space-separated integers: ")
#
# # Convert Input
# numbers_list = [eval(i) for i in input_numbers.split(" ")]
# numbers_tuple = tuple(numbers_list)
# numbers_set = set(numbers_tuple)
# numbers_dict = {}
#
# for index, element in enumerate(numbers_tuple):
#     numbers_dict[index] = element
#
# # Manipulate List
# numbers_list.append(10)
# numbers_list.insert(2, 20)
# numbers_list.remove(8)
#
# # Attempt to Modify Tuple (this will raise an error)
# try:
#     numbers_tuple.append(10)
# except AttributeError:
#     print("Tuples are immutable and cannot be modified.")
#
# # Set Operations
# set_union = numbers_set.union({2, 3, 8})
# set_intersection = numbers_set.intersection({2, 3, 8})
# set_difference = numbers_set.difference({2, 3, 8})
#
# # Dictionary Operations
# print("Original Dictionary:", numbers_dict)
# numbers_dict[10] = 8888
# del numbers_dict[0]
#
# # Type Conversion
# list_to_tuple = tuple(numbers_list)
# list_to_set = set(numbers_list)
# list_to_dict = {}
#
# for index, element in enumerate(numbers_list):
#     list_to_dict[index] = element
#
# tuple_to_list = list(numbers_tuple)
# tuple_to_set = set(numbers_tuple)
# tuple_to_dict = {}
#
# for index, element in enumerate(numbers_tuple):
#     tuple_to_dict[index] = element
#
# set_to_list = list(numbers_set)
# set_to_tuple = tuple(numbers_set)
# set_to_dict = {}
#
# for index, element in enumerate(numbers_set):
#     set_to_dict[index] = element
#
# dict_to_list = list()
# for key, value in numbers_dict.items():
#     dict_to_list.append(value)
#
# dict_to_tuple = tuple(dict_to_list)
# dict_to_set = set()
# for key, value in numbers_dict.items():
#     dict_to_set.add(value)
#
# # Print Output
# print("List to Tuple:", list_to_tuple)
# print("List to Set:", list_to_set)
# print("List to Dictionary:", list_to_dict)
# print("Tuple to List:", tuple_to_list)
# print("Tuple to Set:", tuple_to_set)
# print("Tuple to Dictionary:", tuple_to_dict)
# print("Set to List:", set_to_list)
# print("Set to Tuple:", set_to_tuple)
# print("Set to Dictionary:", set_to_dict)
# print("Dictionary to List:", dict_to_list)
# print("Dictionary to Tuple:", dict_to_tuple)
# print("Dictionary to Set:", dict_to_set)

"""8.
Extend the previous Python program to write the output to a file and perform operations on that file.

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. ...

  h. Write Output to File: Write all the results (original inputs, modified data structures, type conversion results) to a file.

  i. Perform Operations on File: Open the file, read its content, and perform some operations like counting the number of lines, finding specific data, etc.

  j. Modify File Content: Modify the content of the file by, for example, changing specific lines or adding new lines.
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = [eval(i) for i in input_numbers.split(" ")]
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_tuple)
numbers_dict = {}

for index, element in enumerate(numbers_tuple):
    numbers_dict[index] = element

# Manipulate List
numbers_list.append(10)
numbers_list.insert(2, 20)
numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
set_union = numbers_set.union({2, 3, 8})
set_intersection = numbers_set.intersection({2, 3, 8})
set_difference = numbers_set.difference({2, 3, 8})

# Dictionary Operations
print("Original Dictionary:", numbers_dict)
numbers_dict[10] = 8888
del numbers_dict[0]

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = {}

for index, element in enumerate(numbers_list):
    list_to_dict[index] = element

tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = {}

for index, element in enumerate(numbers_tuple):
    tuple_to_dict[index] = element

set_to_list = list(numbers_set)
set_to_tuple = tuple(numbers_set)
set_to_dict = {}

for index, element in enumerate(numbers_set):
    set_to_dict[index] = element

dict_to_list = list()
for key, value in numbers_dict.items():
    dict_to_list.append(value)

dict_to_tuple = tuple(dict_to_list)
dict_to_set = set()
for key, value in numbers_dict.items():
    dict_to_set.add(value)

student_number = input("Enter your student number: ")

# Write Output to File like this:
file = open("numbers.txt", "w")
file.write("Student Number: " + student_number + "\n")
file.write("Original List: " + str(numbers_list) + "\n")
file.write("Original Tuple: " + str(numbers_tuple) + "\n")
file.write("Original Set: " + str(numbers_set) + "\n")
file.write("Original Dictionary: " + str(numbers_dict) + "\n")
file.write("Manipulated List: " + str(numbers_list) + "\n")
file.write("Manipulated Tuple: " + str(numbers_tuple) + "\n")
file.write("Union of Set: " + str(set_union) + "\n")
file.write("Intersection of Set: " + str(set_intersection) + "\n")
file.write("Difference of Set: " + str(set_difference) + "\n")
file.write("Updated Dictionary: " + str(numbers_dict) + "\n")

file.write("List to Tuple: " + str(list_to_tuple) + "\n")
file.write("List to Set: " + str(list_to_set) + "\n")
file.write("List to Dictionary: " + str(list_to_dict) + "\n")
file.write("Tuple to List: " + str(tuple_to_list) + "\n")
file.write("Tuple to Set: " + str(tuple_to_set) + "\n")
file.write("Tuple to Dictionary: " + str(tuple_to_dict) + "\n")
file.write("Set to List: " + str(set_to_list) + "\n")
file.write("Set to Tuple: " + str(set_to_tuple) + "\n")
file.write("Set to Dictionary: " + str(set_to_dict) + "\n")
file.write("Dictionary to List: " + str(dict_to_list) + "\n")
file.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
file.write("Dictionary to Set: " + str(dict_to_set) + "\n")
file.close()

# print "Content of the file:"
print("\n")
fileRead = open("numbers.txt", "r")
print("Content of the file:")
contents = fileRead.read()
print(contents)
fileRead.close()

# Perform Operations on File:
num_lines = contents.count('\n')
print(num_lines)
num_ints = sum(d.isdigit() for d in contents)
print(num_ints)
sum_ints = sum(int(i) for i in contents if i.isdigit())
print(sum_ints)

#   Modify the content of the file
fileModify = open("numbers.txt", "a")
fileModify.write("\nNumber Lines: " + str(num_lines) + "\n")
fileModify.write("Number Ints: " + str(num_ints) + "\n")
fileModify.write("Sum Ints: " + str(sum_ints) + "\n")
fileModify.close()

"""--------------------------------------------------------------------------------
**Control Statements:**
Control statements are used in programming to alter the flow of execution based on certain conditions or criteria. In Python, commonly used control statements include:

`if, elif, else:` These statements are used for conditional execution. They allow the program to execute different blocks of code based on specified conditions.

`for loop:` Used for iterating over a sequence (such as lists, tuples, strings, etc.) or any iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

`while loop:` Used for executing a block of code repeatedly as long as a specified condition is true. It keeps iterating until the condition becomes false.


**Loops:**
Loops are used for executing a block of code repeatedly. In Python, there are two main types of loops:

`for loop: `As mentioned earlier, the for loop iterates over a sequence or any iterable object.

`while loop:` This loop executes a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.

**Other Statements:**
This category typically includes other types of statements that don't fall directly under control statements or loops. It can include various types of statements used for different purposes in Python programming, such as:

`Assignment statements:` Assigning values to variables.

`Function calls:` Invoking functions to perform specific tasks.

`Import statements:` Importing modules or packages to use their functionality in the current script or program.

`Exception handling statements: `Statements used for handling exceptions (errors) that may occur during the execution of a program, such as try, except, finally, etc.

`With statements: `Used for resource management, especially for working with files, to ensure that certain resources are properly closed or released after use.

These are fundamental constructs in Python programming that enable you to control the flow of your program, repeat tasks efficiently, and execute various types of statements to achieve desired functionality.

-------------------------------------------------------------------------------

9.  Utilizing the Largest Integer from output.txt

  Task Description:

  Transform the previous task to utilize the largest integer from the output file 'output.txt' instead of asking the user for it.

  1. Read the largest integer from the 'output.txt' file.
  2. Generate a list of all prime numbers up to the largest integer.
  3. Print the list of prime numbers.
  4. Calculate the sum of all prime numbers in the list.
  5. Determine the largest and smallest prime numbers in the list.
  6. Check if the largest integer itself is prime and print the result.
  7. Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'.
  8. Handle the scenario where the largest integer cannot be found in the file.

  Example:

  If the 'output.txt' file contains:
  Largest prime number: 20

  The program will generate the list of prime numbers up to 20, perform calculations, and write the results to 'prime_numbers.txt'.
"""

"""10.
In the final main.py file, leave the results from task 8 and 9, commit and push
"""
