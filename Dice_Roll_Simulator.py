# Program by Trina Nixon

# assignment parameters are as follows:
# this program will simulate the rolling of two 6-sided dice
# a dictionary will keep track of the # of times that each total # is thrown
# dictionary values are as follows:
# key = sum of the 2 dice
# value = keep track of the # of rolls
# if key does not exist, set the value as 1
# if key does exist, add 1 to the value
# (like in dictionaries assignment)
# if key not in dict:
# value = 1
# else:
# value += 1

# allow user to choose how many times the dice will be thrown
# once dice thrown the specified number of times, print a histogram (using the * character) that shows the total percentage each number was rolled
# each * will represent 1% of the total rolls

# sample session:
# Welcome to the dice throwing simulator!
# How many dice rolls would you like to simulate? 1000

# DICE ROLLING SIMULATION RESULTS
# Each "*" represents 1 % of the total number of rolls.
# Total number of rolls = 1000.
# 2: ***
# 3: ***
# 4: ***********
# 5: ***********
# 6: ********
# 7: ******************
# 8: ****************
# 9: **********
# 10: *************
# 11: *****
# 12: **

# Thank you for using the dice throwing simulator. Goodbye!

# rubric requirements:
# use of a dictionary
# use of loops to iterate dictionary
# use of random number generator

############################################
import random

print("Welcome to the Dice Throwing Simulator!")

# user chooses the number of rolls they want
num_of_rolls = int(input("How many dice rolls would you like to simulate?"))
# print(num_of_rolls)


# initialize dictionary with initial value set to 0 to keep track of total for each number thrown:
# key = sum of 2 dice (2-12)
# value = total number of rolls that equal the key
totals = {}


# user rolls the 2 dice and the results of the roll are added to the dictionary
for i in range(num_of_rolls):
    # dice 1 and dice 2 are rolled and added together
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # print("die 1: ", die1)
    # print("die 2: ", die2)
    total = die1 + die2
    # print("die 1 + die 2: ", total)

    # add these results to the dictionary using a loop to iterate dictionary per rubric
    if total in totals:
        totals[total] += 1
    else:
        totals[total] = 1
    # print(totals)

print("DICE ROLLING SIMULATION RESULTS")
print('Each "*" represents 1% of the total number of rolls')
print("Total number of rolls = ", num_of_rolls)
# print each number 2-12 with the percentage of total rolls each number was
# e.g. 2: ***  (3% of total rolls)
# so take the total for each number and divide by the number of rolls * 100

# e.g. if total of 2 was rolled 7 times out of 100 rolls, then 2: (7/100)*100 = 7 or *******

for i in range(2, 13):
    if i in totals:
        percentage = int(((totals[i]/num_of_rolls)*100))
        print(i, ":", "*" * percentage)
print("Thank you for using the dice throwing simulator. Goodbye!")
