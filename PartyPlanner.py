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
