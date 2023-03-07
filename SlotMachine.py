import math
import random

print("Trina's Slot Machine")
# Player enters the number of tokens they start with
tokens = int(
    input("Please enter the number of tokens you want to start with: "))

# loop that continues until player cashes out or runs out of tokens
while tokens > 0:
    bet = int(input(
        "You can bet 1, 2, or 3 tokens. How much would you like to bet? (enter 4 to cash out): "))
    # if player chooses cash out, then program exits
    if bet == 4:
        print("Thanks for playing! You receive", int(tokens), "tokens.")
        break
    elif bet == 1 or bet == 2 or bet == 3:
        # decrement tokens the amount of bet the player plays
        tokens -= bet
        # chooses a random integer between 1 and 5
        slot1 = random.randrange(1, 6)
        slot2 = random.randrange(1, 6)
        slot3 = random.randrange(1, 6)
    print("[", slot1, "][", slot2, "][", slot3, "]")
# winning slots
    if slot1 == slot2 == slot3:
        # winnings = the number they rolled to the power of their bet
        winTokens = math.pow(slot1, bet)
        # player wins tokens and the win is added to total
        tokens += winTokens
        print("***You win", int(winTokens), "tokens!***")
    else:
        print("You lose", bet, "tokens.")
    print("Tokens: ", int(tokens))
