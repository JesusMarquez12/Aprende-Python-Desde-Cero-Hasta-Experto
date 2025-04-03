# To generate random integer values, one can use the method randint()
# The method receives two parameters, a and b, which are the lower and upper
# bounds of the range where the value is picked from.
# For the method to work, the random module must be imported before the method
# is called.
# To import a module, the syntax is:
# import module_name
# In this case, the module is random, so the import statement is:

# import random

# # Generate a random integer between 1 and 10
# number = random.randint(1, 10)
# print(f"Random number between 1 and 10: {number}")

# # Simulate a six-sided die roll
# die_roll = random.randint(1, 6)
# print(f"Die roll: {die_roll}")

from random import randint    # This is another way to import the method

# Generate a random integer between 1 and 10
number = randint(1, 10)
print(f"Random number between 1 and 10: {number}")

# Simulate a six-sided die roll
die_roll = randint(1, 6)
print(f"Die roll: {die_roll}")



