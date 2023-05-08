import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

# prompt user to choose Rock, Paper, or Scissors.
# check to make sure input is valid, if valid return a string containing the user choice
    def getUserChoice(self):
        while True:
            user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please try again.")
# randomly generate a choice of Rock, Paper, or Scissors for the cpu;
# return a string containing the cpu choice

    def getCPUChoice(self):
        cpu_choice = random.choice(self.choices)
        return cpu_choice
# passed in 2 strings - user_choice and cpu_choice;
# compare the 2 strings and select winner
# return an int that shows winner - 0/tie, 1/user, 2/cpu

    def pickWinner(self, user_choice, cpu_choice):
        if user_choice == cpu_choice:
            return 0
        elif user_choice == 'rock' and cpu_choice == 'scissors':
            return 1
        elif user_choice == 'paper' and cpu_choice == 'rock':
            return 1
        elif user_choice == 'scissors' and cpu_choice == 'paper':
            return 1
        else:
            return 2


        # Main Program
rps = RockPaperScissors()  # ***YOUR CLASS

print("Welcome to Rock, Paper, Scissors!")

hasError = False
numUserWins = 0
numCPUWins = 0

while True:
    try:

        # Reset error checker
        hasError = False

        # Get odd number of games
        numGames = int(input("How many rounds would you like to play? "))

        while numGames % 2 == 0:  # Even number

            print("Sorry, number of games must be odd.  Please try again:")
            numGames = int(input("How many rounds would you like to play?"))

        break

    except ValueError as err:

        hasError = True

        print("Invalid input.  Please enter a number.")


# Play the game for the number of rounds the user entered allowing for ties with the count variable
count = 0
while count < numGames:

    # Get the user and computer choices
    userChoice = rps.getUserChoice()  # ***YOUR METHOD
    cpuChoice = rps.getCPUChoice()  # ***YOUR METHOD

    print("Computer chooses " + cpuChoice)

    # Pick winner
    winner = rps.pickWinner(userChoice, cpuChoice)  # ***YOUR METHOD

    if winner == 0:
        print("It's a tie!  Play again.")
    elif winner == 1:
        print("User wins!")
        numUserWins += 1
        count += 1
    elif winner == 2:
        print("Computer wins!")
        numCPUWins += 1
        count += 1
    else:
        print("Error in picking winner!")

# Print results
print("\n\nUser wins: ", numUserWins)
print("Computer wins: ", numCPUWins)

if numUserWins > numCPUWins:

    print("The user won!")

if numCPUWins > numUserWins:

    print("The computer won!")


# Close game
print("\nThank you for playing!")
