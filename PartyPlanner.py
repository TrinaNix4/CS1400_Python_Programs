"""
print("Welcome to the Treehouse Museum!")

print("What type of party Package would you like: ")
print("1. Playtime Party")
print("2. Deluxe Storybook Party")

party_type = int(input("Enter choice: "))

print("Are you a member of the Treehouse Museum?")
print("1. Yes")
print("2. No")

member = int(input("Enter choice: "))
cost = 0

if party_type == 1 and member == 1:
    cost = 125
elif party_type == 1 and member == 2:
    cost = 160
elif party_type == 2 and member == 1:
    cost = 275
elif party_type == 2 and member == 2:
    cost = 350

print("Your cost would be $", cost)
"""

# Program 1 by Trina Nixon
print("Help Bart Simpson! Use this program to write his sentences for him.")
# get input from user/ sentence and number of times printed
sentence = input("Enter the sentence: ")
num_times = int(input("Enter the number of time to be printed: "))

# print the sentence the number of times the user inputs
for i in range(1, num_times + 1):
    print(str(i) + ': ' + sentence)


###############################################
# Program 2 by Trina Nixon
print("Baggage Check")

# Get input from the user
length = int(input("Enter the length measurement of your luggage: "))
width = int(input("Enter the width measurement your luggage: "))
height = int(input("Enter the heighth measurement of your luggage: "))

# Check if the luggage item meets the size requirements
if length <= 9 and width <= 14 and height <= 22:
    print("Acceptable carry-on item")
else:
    print("Not acceptable as a carry-on item")
