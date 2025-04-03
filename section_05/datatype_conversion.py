# Datatype conversion in Python

# Is also called type casting, some recurrent function to execute this
# process are:

# int() -> Convert some data to integer
# float() -> Convert some data to float
# str() -> Convert some data to string
# bool() -> Convert some data to boolean

# Example script

# Convert string to integer
string_number = "10"
int_number = int(string_number)

print("String to Integer Conversion")
print(f"String number: {string_number}")
print(f"String to Integer number: {int_number}")

# Convert string to float
string_number = "3.14"
float_number = float(string_number)
print("\nString to Float Conversion")
print(f"String number: {string_number}")
print(f"String to Float number: {float_number}")

# Convert integer to string
int_number = 10
string_number = str(int_number)
print("\nInteger to String Conversion")
print(f"\nInteger number: {int_number}")
print(f"Integer to String number: {string_number}")

# Convert to boolean
# Boolean type conversion returns false in the next cases:
# If the value is 0, empty string, or None Type
# Returns true if the value is distint to 0, empty string, or None Type
# Integer conversion
int_number = 0
bool_number = bool(int_number)
print(f"\nBoolean Value of {int_number}: {bool_number}")

int_number = 5
bool_number = bool(int_number)
print(f"Boolean Value of {int_number}: {bool_number}")

# String conversion
string = ""
bool_string = bool(string)
print(f"Boolean Value of an empty string: {bool_string}")

string = "Hello"
bool_string = bool(string)
print(f"Boolean Value of a non-empty string: {bool_string}")

# None Type conversion
none_type = None
bool_none = bool(none_type)
print(f"Boolean Value of None Type: {bool_none}")


