# Example of split method for strings

data = "Hello World!"
my_list = data.split()    # As default, the split method splits the string by whitespace
print(my_list)            # Output: ['Hello', 'World!']

data = "Juan,30,Mexico"
my_list = data.split(",")
print(my_list)            # Output: ['Juan', '30', 'Mexico']