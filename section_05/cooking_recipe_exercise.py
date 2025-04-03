# Cooking recipe

# Create a script that asks the user for some important values for a cooking
# recipe. The script should ask for the following values:
# · Recipe Name
# · Ingredients
# · Cooking Time (in minutes)
# · Dificulty Level ("Easy", "Medium", "Hard")

# Then print the recipe

# Example interaction:
# ***Cooking Recipe***
# Enter the recipe name: > Rainbow Dish
# Enter the ingredients: > quinoa, red cabbage, avocado, carrot and olive oil
# Enter the cooking time (in minutes): > 10
# Enter the difficulty level (Easy, Medium, Hard): > Easy
# --------------------
# Recipe Name: Rainbow Dish
# Ingredients: quinoa, red cabbage, avocado, carrot and olive oil
# Cooking Time: 10
# Difficulty Level: Easy

# Script
print("***Cooking Recipe***")
recipe_name = input("Enter the recipe name: ")
ingredients = input("Enter the ingredients: ")
cooking_time = int(input("Enter the cooking time (in minutes): "))
difficulty_level = input("Enter the difficulty level (Easy, Medium, Hard): ")

# Print the result
print("\n--------------------\n")
print(f"Recipe Name: {recipe_name}")
print(f"Ingredients: {ingredients}")
print(f"Cooking Time: {cooking_time}")
print(f"Difficulty Level: {difficulty_level}")