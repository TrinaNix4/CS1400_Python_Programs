print("Pokemon Trivia")

# initialize counter variables for answers
correct = 0
incorrect = 0

# Question 1
print("Question 1: What type of Pokemon is Pikachu?")
answer = input().lower()
if answer == 'electric':
    print("You are correct!")
    correct += 1
else:
    print("Incorrect. The answer is 'Electric'.")
    incorrect += 1

# prints variable to show user their accumulated score
print("Score:", correct, "out of 5")

# Question 2
print("Question 2: How many evolutions does Eevee have? Please enter a digit 1-10.")
answer = input().lower()
if answer == '8' or answer == 'eight' or answer == 'Eight':
    print("You are correct!")
    correct += 1
else:
    print("Incorrect. The answer is '8'.")
    incorrect += 1

# prints variable to show user their accumulated score
print("Score:", correct, "out of 5")

# Question 3
print("Question 3: What is Piplup's final evolution?")
answer = input().lower()
if answer == 'prinplup':
    print("You are correct!")
    correct += 1
else:
    print("Incorrect. The answer is 'Prinplup'.")
    incorrect += 1

# prints variable to show user their accumulated score
print("Score:", correct, "out of 5")

# Question 4
print("Question 4: What color is Pollywag?")
answer = input().lower()
if answer == 'blue':
    print("You are correct!")
    correct += 1
else:
    print("Incorrect. The answer is 'Blue'.")
    incorrect += 1

# prints variable to show user their accumulated score
print("Score:", correct, "out of 5")


# Question 5
print("Question 5: Who is number 1 in the Pokedex?")
answer = input().lower()
if answer == 'bulbasaur':
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The answer is 'Bulbasaur'.")
    incorrect += 1

# prints variable to show user their accumulated score
print("Score:", correct, "out of 5")

# final stats given to user
print("Quiz Complete!")
print("Number of correct answers:", correct)
print("Number of incorrect answers:", incorrect)
finalPercentage = float(correct / 5)
print('Your final percentage:', finalPercentage * 100, '%')
