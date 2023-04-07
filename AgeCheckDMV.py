print("Welcome to the DMV!")
print("Please use this program to determine if you can apply for a driver's license.")

# checking the age of the user and output if they qualify to apply

while True:
    try:
        # this is dangerous code because they could enter a string
        age = int(input("What is your age?"))
        # if we do get correct input, then force a number greater than 0
        if age <= 0:
            # instead of ValueError, raise a TypeError to give more specific error
            raise TypeError("Enter a number greater than zero.")
        break
        # ValueError gives opportunity to give specific feedback instead of general except
    except ValueError:
        print("Invalid input.")
        print("Please enter your age using numbers. No letters allowed.")
    except TypeError as err:
        # can use the message we passed in above in TypeError
        print(err)
    except:
        print("Invalid input.")
if age < 15:
    print("You cannot apply for a driver's license.")
elif age == 15:
    print("You can apply for a learner's permit.")
elif age >= 16:
    print("You can apply for a driver's license.")
