# Arithmetic operators
# Used to execute simple mathematical calculations

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Float Division (/) : Divide the first operant between the second. The result
#                      is a float value
# Integer Division (//) : Divide the first operant between the second. The 
#                         result is an integer value
# Modulo (%) : Divide the first operant between the second and return the 
#                         constrained number to the range of the second operant.
#                         The result is determined by the operant types. Is
#                         suggested use it only for integer data.
# Power (**): Multiply the first operant with itself n times, where n correspond
#             to the second operant.

a = 10
b = 3

# Addition
addition = a + b
print(f'Addition of {a} and {b}: {addition}')

# Subtraction
sub = a - b
print(f'Subtraction of {b} to {a}: {sub}')

# Multiplication
mult = a * b
print(f'Multiplication of {a} with {b}: {mult}')

# Division
div = a / b
print(f'Division of {a} with {b}: {div:2f}')

# Integer division
int_div = a // b
print(f'Integer part of division from {a} with {b}: {int_div}')

# Modulus operation
mod = a % b
print(f'Carry value of division from {a} with {b}: {mod}')

# Modulus operation
power = a ** b
print(f'The value of {a} powered to {b}: {power}')
