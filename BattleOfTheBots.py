# Program by Trina Nixon

# how the program works:
# battle game between 2 robots
# every time the bots battle, the strength is based off a random number
# (i decide how to set the algorithm for strength)
# the bot with the most strength wins, and the other bots loses life points
# (i decide the algorithm for how much life points they lose)
# life points lost are equal to the difference in strength between bot1 and bot2

# will need access to:
# strength
# life points

###########################################

import random

# create a botPlayer class and instantiate 2 objects of that class for each robot

# instance attributes for the class include: life points, strenght, generator for a random number

# init - a default to set the life point and strength


class BotPlayer:
    def __init__(self):
        # both bots start out with 100 life points
        self.life_points = 100
        self.strength = 10
        self.generator = random.Random()

# behaviors could include:
# set Strength
# receive damage

# algorithm to set strength; generate a random number between 5 and 20
    def set_strength(self):
        self.strength = self.generator.randint(5, 20)

# when a bot is damaged, minus the amt of damage from the bots life pts
    def receive_damage(self, damage):
        self.life_points -= damage

# return a string of botPlayer object that shows life points and strength
# use str() to convert integer to string so it can be concatenated with the string and printed for the user to see
    def __str__(self):
        return "Life Points: " + str(self.life_points) + "\nStrength: " + str(self.strength)

# use while loop so game repeats unless user presses q to quit.


def battle(bot1, bot2):
    while True:
        print("Bot1 Life Points: ", bot1.life_points)
        print("Bot2 Life Points: ", bot2.life_points)

        print("Bot1, it's your turn!")
        choice = input("Press 'h' to hit, or 'q' to quit: ")

        if choice == 'q':
            break

        bot1.set_strength()
        bot2.set_strength()

        print("Bot1 strength: ", bot1.strength,
              "Bot2 strength: ", bot2.strength)

# amt of damge is equal to the difference in strength between 2 bots
        if bot1.strength > bot2.strength:
            damage = bot1.strength - bot2.strength
    # bot1 has more strength, so bot2 receives the damage
            bot2.receive_damage(damage)
            print("Bot2 has", damage, "points of damage.")
    # bot2 has more strength, so bot1 receives the damage
        elif bot2.strength > bot1.strength:
            damage = bot2.strength - bot1.strength
            bot1.receive_damage(damage)
            print("Bot1, you have", damage, "points of damage.")
        else:
          # in case there is a tie
            print("It's a tie!")
  # if either bot loses all of their life points, break from program
        if bot1.life_points <= 0 or bot2.life_points <= 0:
            break

# repeat the same process above for bot2
        print("Bot2, it's your turn!")
        choice = input("Press 'h' to hit, or 'q' to quit: ")

        if choice == 'q':
            break
        bot1.set_strength()
        bot2.set_strength()

        print("Bot1 strength: ", bot1.strength,
              "Bot2 strength: ", bot2.strength)

        if bot2.strength > bot1.strength:
            damage = bot2.strength - bot1.strength
            bot1.receive_damage(damage)
            print("Bot1, you have", damage, "points of damage.")
        elif bot1.strength > bot2.strength:
            damage = bot1.strength - bot2.strength
            bot2.receive_damage(damage)
            print("Bot2, you have", damage, "points of damage.")
        else:
            print("it's a tie!")

        if bot1.life_points <= 0 or bot2.life_points <= 0:
            break

    print("Nice battle!")
    if bot1.life_points < bot2.life_points:
        print("Bot2 wins this round!")
    elif bot1.life_points == bot2.life_points:
        print("It's a tie!")
    else:
        print("Bot1 wins this round!")

    print("Thanks for playing!")


# main program
bot1 = BotPlayer()
bot2 = BotPlayer()

battle(bot1, bot2)
