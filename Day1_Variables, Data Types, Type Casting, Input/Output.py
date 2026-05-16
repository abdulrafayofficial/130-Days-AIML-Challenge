#Question: Ask user for name, age, height. Print
#formatted bio + auto-convert height to feet.

name = input("Enter Your Name: ")
height = int(input("Enter Your Height in Inches: "))

height_in_feet = height / 12

print(f"Your name is {name} and your height is {height} inches.")
print(f"{name}, your height in feet is {height_in_feet : .2f}")
