# In python, there is not a specific type to define a constant, only a
# convention can be used.

# This convention is to use UPPERCASE to indicate that the variable is
# expected to be used as a constant and is recommended to not edit their
# value

# Example

import math

print('*** Python Constants ***')

PI = 3.14159
print("Pi's value is:", PI)

DATABASE_NAME = 'db_clients'
print("The database's name is:", DATABASE_NAME)

# This is a example of what MUST NOT BE done, do not modify a constant
# value

DATABASE_NAME = 'db_clients_list'
print("The database's name is:", DATABASE_NAME)

# Use a constant of the python language, even if is not in UPPERCASE
print("Math Pi's value is:", math.pi)