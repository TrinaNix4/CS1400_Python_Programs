import math
import random

print("Trina's Slot Machine")
tokens = int(
    input("Please enter the number of tokens you want to start with: "))


bet = int(input(
    "You can bet 1, 2, or 3 tokens. How much would you like to bet? (enter 4 to cash out): "))
while bet == 1 or bet == 2 or bet == 3:
    # decrement tokens the amount of bet the player plays
    tokens -= bet
    slot1 = random.randint(1, 5)
    slot2 = random.randint(1, 5)
    slot3 = random.randint(1, 5)
    print(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        # the number they rolled to the power of their bet
        winTokens = math.pow(slot1, bet)
        # player wins tokens and the win is added to total
        tokens += winTokens
        print("You win ", winTokens, "tokens!")
    else:
        print("You lose ", bet, "tokens.")
print("Tokens: ", tokens)
