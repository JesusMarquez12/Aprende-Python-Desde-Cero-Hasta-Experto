# Employee System

# Script that prompt the user for the next data:
# - Employee name
# - Employee age (convert to int)
# - Employee salary (convert to float)
# - Is a department chief? (Yes or No)

# Script

print("*** Employee System ***")
employee_name = input("Enter employee name: ")
employee_age = int(input("Enter employee age: "))
employee_salary = float(input("Enter employee salary: "))
is_department_chief = input("Is a department chief? (Yes or No): ").strip().lower()

# Convert to boolean the var is_department_chief
is_department_chief = is_department_chief.lower() == 'yes'

# Print employee values
print("\n*** Employee Data ***")
print(f"Name: {employee_name}")
print(f"Age: {employee_age}")
print(f"Salary: {employee_salary:.2f}")
print(f"Is department chief?: {is_department_chief}")
