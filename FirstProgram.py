# Program 1 by Trina Nixon

print("Welcome to Mad Libs")

# get user input for each item in the mad lib
verb = input("Enter a verb: ")
animal = input("Enter an animal: ")
object1 = input("Enter an object: ")
object2 = input("Enter another object: ")

# print results
print("Twinkle twinkle, little", animal, '. How I wonder where you', verb, '. Up above the', object1,
      'so high. Like a', object2, 'in the sky. Twinkle twinkle, little', animal, 'how I wonder what you', verb, '.')

######################################
# Program 2 by Trina Nixon
print("Welcome to your Baseball Teams Calculator.")

# get input from user
num_students_in_class = int(
    input("Enter the number of students in your class: "))

# calculate the number of teams and any leftovers
# baseball teams have 9 players
# use int division so no decimals

num_teams = num_students_in_class // 9
num_extra_players = num_students_in_class % 9

# results displayed
print("There can be", num_teams, 'teams with',
      num_extra_players, 'extra players.')
