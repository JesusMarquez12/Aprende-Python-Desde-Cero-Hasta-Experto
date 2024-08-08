# Example of values declaration and assignation
# name = "Maria"
# age = 30
# weight = 65.5
# is_married = False

age = 28
height = 1.65
country = 'Mexico'

# Access to variables
print('Initial Values')
print('Age:', age)
print('Height:', height)
print('Country:', country)

# Modify variable value
age = 30
height = 1.68

# Access to variables
print('Modified Values')
print('Age:', age)
print('Height:', height)
print('Country:', country)

# Python have dynamic typing
age = 'thirty'
print('Modified Values')
print('Age:', age)

# If a non declared value is accessed, a error is throw
print('Phone Number:', phone_number)