# By Trina Nixon
# Program will allow user to input a sentence. It will take the first letter of each word and create an acronym
# Example: Random Access Memory: RAM
# Example: Laugh Out Loud: LOL

print("Acronym Maker")
# put into a loop so continuously goes until our sentence equals q
sentence = ""
while sentence != "q":
    sentence = input("Enter a sentence, or q to quit: ")
    pos = 0
    acronym = sentence[0]
    # so long as pos is greater or equal to 0, keep repeating this code
    while pos >= 0:
        # starts at pos instead of just the beginning
        pos = sentence.find(" ", pos)
        if pos >= 0 and sentence != 'q':
            # gets us to the character immediately after the space pos
            pos += 1
            # add the letter onto our acronym
            acronym += sentence[pos]
    if sentence != 'q':
        # prints our acronym in upper case
        print("Acronym: ", acronym.upper())
