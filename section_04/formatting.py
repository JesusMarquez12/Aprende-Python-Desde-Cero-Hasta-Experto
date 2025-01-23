# String formatting

# Since Python 3.6, use of f-string
variable = 'World'
result = f'Hello {variable}.'
print(result)

# Since Python 2.7, use format method
result = 'Hello {}.'.format(variable)
print(result)

# Another example

name = 'Juan'
age = 30

# f-string
message = f'Hello, my name is {name} and i\'m {age} years old.'
print(message)

# format method
message = 'Hello, my name is {} and i\'m {} years old.'.format(name,age)
print(message)