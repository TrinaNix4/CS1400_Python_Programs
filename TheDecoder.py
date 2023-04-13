# variable to store the decryption key
dKey = 0

while True:
    try:
        print('Please enter the key used to decrypt the file.')
        # if it is not a number, will raise an exception
        dKey = int(input())
        break
    except ValueError:
        print("Please enter a number.")
        print("Please try again")


while True:
    try:
        print("Please enter the file you would like to decrypt.")
        fileName = input()

        # want program to go into file that is entered by user, get each characters and decrypt them using the decryption key and then write all of this to new file

    # attempt to open file and read from it
        f = open(fileName, 'r')

    # if file doesnt exist, when 'w' is used it will create the file
    # createa  file to write the decrypted text to
        decryptedFile = open('decrypted.text', 'w')

        for line in f:
            # gives us the length of the line
            for i in range(len(line)):
                # getting each character in the string
                letter = line[i]
        # getting the value of the letter
                chValue = ord(letter)
        # subtracting the decryption key
                chValue -= dKey
        # converting value back into a letter
                letter = chr(chValue)
        # writing it back to the file
                decryptedFile.write(letter)
        # if all this in the 'try' works, need to break
        break
    # if file doesn't exist, will fall into an except
    except FileNotFoundError:
        print("File does not exist. Please enter a correct file name.")
    # general except
    except:
        print("Error occurred")

print('File was decrypted to decrypted.txt')
f.close()
decryptedFile.close()
