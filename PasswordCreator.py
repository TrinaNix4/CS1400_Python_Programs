# Program by Trina Nixon
fName = input("Enter first name: ")
lName = input("Enter last name: ")
wNum = input("Enter W number: ")

fLen = len(fName)

username = fName[0].lower() + lName[0].lower() + wNum[4:9]
password = fName[0].upper() + fName[1: fLen].lower() + "cs!"


print("Username: ", username)
print("Password: ", password)
