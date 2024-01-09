import random

# Generate a random number between 0 and 10
number = random.randint(0, 10)

# Print the generated number
print(number)

# Check if the number is greater than 6
if number > 6:
    print("big number 1")  # If it is, print "big number 1"
    print("big number 2")  # Then print "big number 2"
    print("big number 3")  # Finally, print "big number 3"

# Print the string "number"
print("number")

# Check if the number is greater than 8
if number > 8:
    print("really big number 4")  # If it is, print "really big number 4"
# If the number is not greater than 8, check if it's greater than 6
elif number > 6:
    print("big number 4")  # If it is, print "big number 4"

# Print the string "number again"
print("number again")

thresh = 6

# Check if the number is greater than the threshold (6)
if number > thresh:
    print("big number")  # If it is, print "big number"
# If the number is not greater than the threshold, check if it's less than the threshold
elif number < thresh:
    print("small number")  # If it is, print "small number"
else:  # If the number is equal to the threshold
    print("number is {}".format(thresh))  # Print "number is 6" with the actual threshold value.
