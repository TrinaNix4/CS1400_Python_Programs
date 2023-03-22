import random

print("Mastermind")
secret = []
for i in range(4):
    secret.append(random.randrange(1, 5))

posCorrect = 0
guesses = 0
maxGuesses = 15

# keep game going until win or lose
while posCorrect < 4 and guesses < maxGuesses:
    # allow user to guess 4 numbers
    guessArrayString = input("Enter your guess of 4 numbers: ").split()
    print(guessArrayString)
    # splits the 4 number and creates an array of 4 values
    guesses += 1

# cast guessArrayString it as an array of ints
    guessArrayInt = [int(i) for i in guessArrayString]
    print(guessArrayInt)

# create copies
    tempSecret = secret.copy()
    tempGuessInt = guessArrayInt.copy()
    posCorrect = 0
# positions correct
    for i in range(len(tempSecret)):
        if tempSecret[i] == tempGuessInt[i]:
            posCorrect += 1
            tempSecret[i] = -1
            tempGuessInt[i] = -1
    colorsCorrect = 0

    for i in range(len(tempSecret)):
        for j in range(len(tempGuessInt)):
            if i != j and tempSecret[i] == tempGuessInt[j] and tempSecret[i] != -1:
                colorsCorrect += 1
                tempSecret[i] = -1
                tempGuessInt[i] = -1
                break

    print("positions correct: ", posCorrect)
    print("Colors correct: ", colorsCorrect)

    if posCorrect == 4:
        print("you win!")
    elif guesses == maxGuesses:
        print("you lose!")

print("Secret combo was: ", secret)
