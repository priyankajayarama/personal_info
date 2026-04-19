# Personal Information Manager
# My first Python project
# Author: [Your Name]
# Description: Stores and displays personal information using variables,
#              user input, and formatted output.

# ---------- Welcome message ----------
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# ---------- Store static information ----------
name = "Priyanka Jayarama"        # Your full name (string)
age = 22                     # Your age in years (integer)
city = "Vijayawada"       # City you live in (string)
hobby = "playing guitar"     # Something you enjoy doing (string)

# ---------- Get user input ----------
print("Please tell me about yourself:")
print("-" * 30)

# Ask for favorite food, and keep asking if input is empty
favorite_food = input("What's your favorite food? ")
while favorite_food.strip() == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

# Ask for favorite color, and keep asking if input is empty
favorite_color = input("What's your favorite color? ")
while favorite_color.strip() == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# ---------- Calculations ----------
age_in_months = age * 12

# ---------- Display all information ----------
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name:           {name}")
print(f"Age:            {age} years ({age_in_months} months old)")
print(f"City:           {city}")
print(f"Hobby:          {hobby}")
print()
print(f"Favorite Food:  {favorite_food.capitalize()}")
print(f"Favorite Color: {favorite_color.capitalize()}")
print()

# ---------- Goodbye message ----------
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)