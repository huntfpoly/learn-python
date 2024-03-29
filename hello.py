name = input("What is your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
# name = name.title()

# Capitalize first letter of user's name
# name = name.capitalize()

# Split user's name into first and last name
first = name.split()

print(f"Hello, {first}!")
