# Print the party options for user to choose from
while True:
    print("Welcome to the Dinosaur Park Party Planner. Please choose the type of party: ")
    print("1. Group Rate Admission Party")
    print("2. Bare Bones Package")
    print("3. Deluxe Party Package")
    print("4. Quit")
# Stores user choice in variable named choice
    choice = int(input("Enter choice: "))
# Exits loop if user chooses 4
    if choice == 4:
        print("Come back soon!")
        break
# Asks for user input on their member status 1-yes 2-no
    memberStatus = int(
        input("Are you a member? Press 1 for 'yes' and 2 for 'no': "))
    print("The base cost covers admission for up to 12 guests.")
# Stores user input of # of additional adults in variable
    numOfAdditionalAdult = int(
        input("Enter the number of additional adults: "))
# Stores user input of # of additional children in variable
    numOfAdditionalChild = int(
        input("Enter the number of additional children: "))

# Group Rate for members
    if choice == 1 and memberStatus == 1:
        package = "Group Rate Admission Party at Member Rates"
        cost = ((numOfAdditionalAdult * 5) + (numOfAdditionalChild * 4))
# Bare Bones Package for members
    elif choice == 2 and memberStatus == 1:
        package = "Bare Bones Package at Member Rates"
        cost = (99 + (numOfAdditionalAdult * 3) + (numOfAdditionalChild * 3))
# Deluxe Party for members
    elif choice == 3 and memberStatus == 1:
        package = "Deluxe Party at Member Rates"
        cost = (175 + (numOfAdditionalAdult * 3) + (numOfAdditionalChild * 3))
# Group Rate for non-members
    elif choice == 1 and memberStatus == 2:
        package = "Group Rate Admission Party at Non-member Rates"
        cost = ((numOfAdditionalAdult * 5) + (numOfAdditionalChild * 4))
# Bare Bones Package for non-members
    elif choice == 2 and memberStatus == 2:
        package = "Bare Bones Package at Non-member Rates"
        cost = (119 + (numOfAdditionalAdult * 3) + (numOfAdditionalChild * 3))
# Deluxe Party for non-members
    elif choice == 3 and memberStatus == 2:
        package = "Deluxe Party at Non-member Rates"
        cost = (199 + (numOfAdditionalAdult * 3) + (numOfAdditionalChild * 3))
# Prints if user selects any choice other than 1, 2, or 3
    else:
        print("Come back soon!")
# Output of total cost for user
    print("You have selected", package, "for a total cost of $", cost, ". Your total cost includes 12 guests with",
          numOfAdditionalAdult, "additional adults, and", numOfAdditionalChild, "additional children.")
