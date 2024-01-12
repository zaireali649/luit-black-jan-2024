import random

# Create an empty dictionary 'var'
var = {}

# Print the type of 'var' (it will be a dictionary)
print(type(var))

# Create a dictionary 'var2' with key-value pairs
var2 = {"fruit": "mango", "juice": "cranberry", "weather": "snow"}

# Print the contents of 'var2'
print(var2)

# Access and print the value associated with the key "juice"
print(var2["juice"])

# Add a new key-value pair "drank" -> "margarita" to 'var2'
var2["drank"] = "margarita"

# Print 'var2' after adding a new key-value pair
print(var2)

# Delete the key "drank" and its associated value from 'var2'
del var2["drank"]

# Print 'var2' after deleting the key
print(var2)

# Print the list of available methods for 'var2' (dictionary)
print(dir(var2))

# Print the keys of 'var2'
print(var2.keys())

# Print the type of 'var2.keys()' (it's a dict_keys object)
print(type(var2.keys()))

# Convert the dict_keys object to a list and print it
print(list(var2.keys()))

# Print the values of 'var2'
print(var2.values())

# Print the type of 'var2.values()' (it's a dict_values object)
print(type(var2.values()))

# Convert the dict_values object to a list and print it
print(list(var2.values()))

# Print the key-value pairs of 'var2' as tuples
print(var2.items())

# Print the type of 'var2.items()' (it's a dict_items object)
print(type(var2.items()))

# Convert the dict_items object to a list of tuples and print it
print(list(var2.items()))

# Iterate through the key-value pairs of 'var2' and print them
for k, v in var2.items():
    print(k, v)

# Create a dictionary 'dict_of_lists' with keys and lists of random integers as values
dict_of_lists = {i: [random.randint(0, 10) for j in range(3)] for i in range(3)}

# Print 'dict_of_lists'
print(dict_of_lists)

# Iterate through 'dict_of_lists', printing each key and its associated list of numbers
for k, numbers in dict_of_lists.items():
    print(k, numbers)
    for number in numbers:
        print(number)
