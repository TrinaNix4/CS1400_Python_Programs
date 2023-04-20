# Program by Trina Nixon
import math

print("Welcome to Weber State University Human Performance Lab")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI")
print("The program will also store this information in a file you choose so that it can be tracked over time.")


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
            raise TypeError("Invalid inches value. Must be a positive number.")
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
            raise TypeError("Invalid pounds value. Must be a positive number.")
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
