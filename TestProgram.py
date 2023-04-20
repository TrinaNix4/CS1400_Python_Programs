import math

print("Welcome to Weber State University Human Performance Lab")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI")
print("The program will also store this information in a file you choose so that it can be tracked over time.")

# prompt user for file name and option
while True:
    try:
        option = int(input(
            "Enter 1 to create a new file, 2 to open an existing file, or 3 to read from a file: "))
        if option not in [1, 2, 3]:
            raise ValueError("Invalid option. Must be 1, 2, or 3.")
        break
    except ValueError:
        print("Invalid option. Must be 1, 2, or 3.")

filename = input("Enter the filename: ")

if option == 1:
    # create a new file
    file = open(filename, "w")
elif option == 2:
    # open an existing file to add results
    file = open(filename, "a")
elif option == 3:
    # read results from a file
    try:
        file = open(filename, "r")
        for line in file:
            print(line.strip())
        file.close()
    except FileNotFoundError:
        print("File not found.")

# prompt user for age
# make sure user enters only positive numbers, no strings
while True:
    try:
        age = int(input("Enter age in years: "))
        if age <= 0:
            raise ValueError("Invalid age. Must be a positive number.")
        break
    except ValueError:
        print("Invalid age. Must be a number.")

# prompt user for height
# make sure user enters only positive numbers, no strings
while True:
    try:
        height = float(input("Enter height in inches: "))
        if height <= 0:
            raise ValueError(
                "Invalid inches value. Must be a positive number.")
        break
    except ValueError:
        print("Invalid inches value. Must be a number.")

# prompt user for weight
# make sure user enters only positive numbers, no strings
while True:
    try:
        weight = float(input("Enter weight in pounds: "))
        if weight <= 0:
            raise ValueError(
                "Invalid pounds value. Must be a positive number.")
        break
    except ValueError:
        print("Invalid pounds value. Must be a number.")

# print new line
print("\n")

print("Age:", age, "years")
print("Height:", height, '"')
print("Weight:", weight, "pounds")

# print new line
print("\n")

# calculate max heart rate and fat-burning heart rate

# max rate: 220 - age
max_hr = 220 - age
# print("Max heart rate: ", max_hr)

# fat burning heart rate => 70% of max
fat_burning_hr = 0.7 * max_hr
print("Fat burning Heart Rate:", (round(fat_burning_hr)), "bpm")

# calculate BMI:
# BMI = 703 x weight(lbs) / [height(in)]^2
bmi = 703 * weight / (height ** 2)
print("Body Mass Index:", (round(bmi, 1)))

# write results to file
if option == 1 or option == 2:
    file.write(f"Age: {age} years, Height: {height} inches, Weight: {weight} pounds, Fat burning Heart Rate: {round(fat_burning_hr)} bpm, Body Mass Index:
