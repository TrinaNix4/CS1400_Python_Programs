import random


class Cootie:
    def __init__(self):
        self.messages = [
            "Positively Not", "Outlook Not So Good", "Maybe, Maybe Not", "Signs Point to Yes", "It is certain", "Don't Count On It", "Ask again later", "Absolutely"
        ]
        self.final_choice = None

    def makeChoice(self):
        print("Welcome to Cootie Catcher!")
        question = input("Ask the Cootie Catcher any question: ")
        color = input("Choose a color (red, yellow, green, or blue): ").lower()

        while color not in ["red", "yellow", "green", "blue"]:
            print("Sorry, that is not a valid option.")
            color = input("Choose a color (red, yellow, green, or blue): ")

        if len(color) % 2 == 0:
            options = [1, 2, 5, 6]
            option_text = "1, 2, 5, 6"
        else:
            options = [3, 4, 7, 8]
            option_text = "3, 4, 7, 8"

        while True:
            try:
                number = int(input(f"Choose a number ({option_text}): "))
                if number not in options:
                    print("Sorry, that number is not a valid option. Choose again.")
                else:
                    break
            except ValueError:
                print(
                    "Sorry, that is not a valid number. Please enter your choice in numeric format.")

        self.final_choice = random.choice(self.messages)
        print("Cootie says:", self.final_choice)

        play_again = input("Would you like to (p)lay again or (q)uit?")

        while play_again.lower() not in ["p", "q"]:
            print("Sorry, that is not a valid option.")
            play_again = input("Would you like to (p)lay again or (q)uit?")

        if play_again == "p":
            self.makeChoice()


cootie_catcher = Cootie()
cootie_catcher.makeChoice()
