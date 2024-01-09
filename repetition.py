import random

# Generate a random number between 0 and 10
number = random.randint(0, 10)

# Set the threshold value to 7
thresh = 7

# Initialize a counter variable to 0
counter = 0

# Start a while loop that continues until 'number' equals 'thresh'
while number != thresh:
    # Generate a new random number between 0 and 10
    number = random.randint(0, 10)
    
    # Increase the counter by 1 (equivalent to counter += 1)
    counter = counter + 1  # Increment the counter
    
    # Check if the counter is greater than or equal to 15
    if counter >= 15:
        break  # Exit the loop if the counter reaches 15 or more

# Print the counter value and the final number
print("counter: {} number: {}".format(counter, number))

# Start a for loop that iterates from 0 to 9
for i in range(10):
    print(i**2)  # Print the square of the current value of 'i'

# Start a for loop that iterates from 0 to 2 (3 times)
for i in range(3):
    print("Hi from for loop")  # Print "Hi from for loop" each time

# Start a for loop that iterates from 0 to 9
for i in range(10):
    # Check if the cube of 'i' is less than 250
    if i**3 < 250:
        print(i**3)  # If it is, print the cube of 'i'
    else:
        # If the cube is too large, print a message
        print("i cubed too large for {}".format(i))
