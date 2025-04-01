# Input method characteristics

# Interactivity: Allow user to provide input during program execution.
# Easy to use: Input method only need to indicate the string to show to the
# user, to explain what is expected.
# Datatype: Input method always returns a string, so the user must convert
# the input to the desired type, if needed

# Example: Data input by console

name = input('Ingress your name: ')
print(f"Received the value for name variable: {name}")

# Ask the user age and convert it to an integer
age = int(input('Ingress your age: '))

print(f"Your age is: {age}, and in one year you will be {age + 1} years old")