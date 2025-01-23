# Substring handling

# Define a string
string = "Hello, World!"

#########################################################
# String slicing process
#########################################################

# Retrieve substring from hello using index from 0 to 5, since 5 is excluded
hello_substring = string[0:5]
print(f'Hello substring: {hello_substring}')

# Retrieve substring from world using index from 7 to 12
world_substring = string[7:12]
print(f'World substring: {world_substring}')

#########################################################
# Find method
#########################################################

world_index = string.find('World')
print(f'World Substring index: {world_index}')

# Find method return index of the first occurrence of the substring
string_2 = "Hello, World, World World!"
world_index_2 = string_2.find('World')
print(f'World Substring index from string 2: {world_index_2}')

# Find method is case sensitive
hello_index = string.find('hello')

# When the substring is not found, the find method returns -1
print(f'Hello Substring index: {hello_index}')

