import random

# Create an empty list 'var'
var = []

# Print the type of 'var' (it will be a list)
print(type(var))

# Create a list 'var2' containing integers and a string
var2 = [151, 251, 386, 493, 649, "009"]

# Print the contents of 'var2'
print(var2)

# Append the integer 721 to 'var2'
var2.append(721)  # Equivalent to var2 = var2 + [721]

# Print 'var2' after appending
print(var2)

# Print the list of available methods for 'var2'
print(dir(var2))

# Reverse the order of elements in 'var2'
var2.reverse()

# Print 'var2' after reversing
print(var2)

# Create a range object 'numbers' from 0 to 4 (exclusive)
# (In Python 3, 'range' returns a range object, not a list)
numbers = range(5)

# Print 'numbers'
print(numbers)

# Print the type of 'numbers' (it's a range object)
print(type(numbers))

# Convert the 'numbers' range object to a list
numbers = list(numbers)

# Print the type of 'numbers' (now it's a list)
print(type(numbers))

# Print the contents of 'numbers' (a list of integers from 0 to 4)
print(numbers)

# Iterate through 'numbers' and print the square of each number
for number in numbers:
    print(number**2)

# Create a list 'var3' with 5 random integers between 0 and 10
var3 = [random.randint(0, 10) for i in range(5)]

# Print 'var3'
print(var3)

# Print the element at index 2 of 'var3'
print(var3[2])

# Print the length of 'var3'
print(len(var3))

# Create a list of lists 'list_of_lists' with 3 sublists, each containing 3 random integers
list_of_lists = [[random.randint(0, 10) for i in range(3)] for j in range(3)]

# Print 'list_of_lists'
print(list_of_lists)

# Iterate through 'list_of_lists', printing each sublist and its elements
for element in list_of_lists:
    print(element)
    for number in element:
        print(number)
