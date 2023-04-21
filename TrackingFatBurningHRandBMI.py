# Program by Trina Nixon
import math


print("Welcome to Weber State University Human Performance Lab.")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI.")
print("The program will also store this information in a file you choose so that it can be tracked over time\n")

while True:

    # prompt user to choose option 1, 2, or 3. incude a try except block in case they choose a number other than 1, 2, or 3
    while True:
        try:
            option = int(input(
                "Select:\n 1. Create a file \n 2. Open a file to add results to \n 3. Read results from file \n"))
            if option not in [1, 2, 3]:
                raise ValueError(
                    "Invalid selection. Choose option 1, 2, or 3.")
            break
        except ValueError:
            print("Invalid selection. Must be 1, 2, or 3.")
# create variable for filename to read, write or append to
    filename = input(
        "Enter the name of the file you would like to access or create: \n")

# if user chooses 1, create a new file; open() with a "w"
    if option == 1:
        file = open(filename, "w")

# if user chooses 2, open an existing file to add to; open with an 'a'
    elif option == 2:
        file = open(filename, "a")
# if user chooses 3, read results from a file; open with an 'r'
    elif option == 3:
        try:
            file = open(filename, "r")
            for line in file:
                print(line.strip())
            file.close()
        except FileNotFoundError:
            print("File not found.")
        break
# prompt user for age
# make sure user enters only positive numbers, no strings
    while True:
        try:
            age = int(input("Enter age in years: "))
            if age <= 0:
                raise TypeError("Invalid age. Must be a positive number.")
            break
        except ValueError:
            print("Invalid age. Must be a number.")
        except TypeError as err:
            print(err)

# prompt user for height
# make sure user enters only positive numbers, no strings
    while True:
        try:
            height = float(input("Enter height in inches: "))
            if height <= 0:
                raise TypeError(
                    "Invalid inches value. Must be a positive number.")
            break
        except ValueError:
            print("Invalid inches value. Must be a number.")
        except TypeError as err:
            print(err)

# prompt user for weight
# make sure user enters only positive numbers, no strings
    while True:
        try:
            weight = float(input("Enter weight in pounds: "))
            if weight <= 0:
                raise TypeError(
                    "Invalid pounds value. Must be a positive number.")
            break
        except ValueError:
            print("Invalid pounds value. Must be a number.")
        except TypeError as err:
            print(err)
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


# write results of calculations to the file;
# use \n to put each entry on a new line
    if option == 1 or option == 2:
        file.write(f"FBHR: {round(fat_burning_hr)} - BMI {round(bmi, 1)}\n")

    print("Results added to file.\n")

    file.close()
