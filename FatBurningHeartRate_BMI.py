# Program by Trina Nixon

print("Welcome to Weber State University Human Performance Lab")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI")

# prompt user for age
# make sure user enters only positive numbers, no strings
while True:
    try:
        age = int(input("Enter age: "))
        if age <= 0:
            raise TypeError("Invalid age. Enter a number greater than zero.")
        break
    except ValueError:
        print("Invalid age. Must be a number.")
    except TypeError as err:
        print(err)

while True:
    try:
        height = float(input("Enter height in inches: "))
        if height <= 0:
            raise TypeError("Invalid inches value. Must be greater than 0.")
        break
    except ValueError:
        print("Invalid height. Must be a number.")
    except TypeError as err:
        print(err)
