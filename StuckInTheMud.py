# Program by Trina Nixon

import random
print("Welcome to Stuck in the Mud")

# how to play:
# players rolls five dice
# 2s and 5s do not count as any points and are now "stuck in the mud"
# the remaining dice are added up as the score for that throw
# any 2s or 5s are set aside and the remaining dice are thrown again
# again, if any 2s or 5s, those dice are "stuck in the mud"
# remaining dice added to the score
# continue doing this until all dice are "stuck in the mud"
# print total score

# sample session
# Stuck in the Mud
# Press r to roll or q to quit: r
# You rolled:  [5, 4, 5, 1, 6]
# Score:  11

# Press r to roll or q to quit: r
# You rolled:  [5, 2, 5, 1, 6]
# Score:  18

# Press r to roll or q to quit: r
# You rolled:  [5, 2, 5, 3, 3]
# Score:  24

# Press r to roll or q to quit: r
# You rolled:  [5, 2, 5, 5, 3]
# Score:  27

# Press r to roll or q to quit: r
# You rolled:  [5, 2, 5, 5, 3]
# Score:  30

# Press r to roll or q to quit: q
# Thanks for playing

#########################################

# include to print random numbers and simulate a dice roll

# create an empty list
dice = [0, 0, 0, 0, 0]
# initialize score variable to keep track of player score
score = 0
rollScore = 0
# roll 5 dice
for i in range(5):
    dice[i] = random.randint(1, 6)
# use a while loop to continue playing game until player presses q to quit
while True:
    rollScore = 0
    choice = input("Press r to roll or q to quit: ")
    if choice == 'q' or choice == 'Q':
        print("Thanks for playing!")
        break

    for i in range(5):
        if dice[i] != 2 and dice[i] != 5:
            dice[i] = random.randint(1, 6)

# calculate the score - sum all the values of dice that are
# not equal to 2 or 5
# loop through dice, which has 5 integers(values of dice)
# check if it's not equal to 2 or 5, the value is added to
# score
    for i in range(5):
        if dice[i] != 2 and dice[i] != 5:
            # rollScore variable to keep track of a 0 score and exit program
            rollScore += dice[i]
    score += rollScore
# print the result of roll
    print('You rolled: ', dice)
# print the score
    print("Score: ", score)
# since it doesn't add 2s or 5s to score, when rollScore = 0 all
# dice are stuck in the mud
    if rollScore == 0:
        print("All dice are stuck in the mud. Thanks for playing!")
        break
