# By Trina Nixon
# This program checks whether a user-entered variable name is proper:
# 1 - checks if illegal - no spaces allowed and must begin with a letter
# 2 - legal, but poor style (should use only letter or digits
# 3 - good


print("This program checks the properness of a proposed variable name.")

# user inputs a variable name
varName = ""
# program loops unless user enters a q to quit
while varName != 'q':
    varName = input("Enter a variable name, or q to quit: ")

# check if spaces in user-entered name and check if it begins with a letter
    if ' ' in varName or not varName[0].isalpha():
        print("Variable name is illegal! Variable name must begin with a letter and must not contain any spaces.")
    else:
        # if legal, also check if proper style - uses only letter or digits
        if not varName.isalnum():
            print(
                "Variable name is legal, but in poor style. Should contain only letters or numbers.")
        else:
            print("Variable name is good!")
