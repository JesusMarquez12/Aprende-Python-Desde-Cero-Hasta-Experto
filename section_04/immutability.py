# Immutability in strings
string_1 = 'Hello World'
# string_1[0] = 'h'       # Is not possible to edit characters from the string
string_2 = string_1       # string_2 acts as a pointer to the content of string_1
string_1 = 'Bye'
print(string_1)
print(string_2)