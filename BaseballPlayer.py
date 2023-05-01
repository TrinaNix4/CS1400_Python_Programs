
class BaseballPlayer:

    def __init__(self):
        self.name = "none"
        self.number = "none"
        self.batting_avg = 0

# being passed as arguments and being set here as parameters of this method
    def calculate_batting_avg(self, incoming_hits, incoming_at_bats):
        self.batting_avg = round(incoming_hits / incoming_at_bats, 3)
        return self.batting_avg


# main program
print("Welcome to the Player Tracker!")

# enter the name of the player and their number and a function will calculate the batting average
playerName = input("What is the player's name?")
playerNumber = input("What is the player's number?")

myPlayer = BaseballPlayer()
myPlayer.name = playerName
myPlayer.number = playerNumber

hits = int(input("How many hits did the player get?"))
at_bats = int(input("How many times were they up to bat?"))
print(myPlayer.calculate_batting_avg(hits, at_bats))
