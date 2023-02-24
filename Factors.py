# Program to display all the factors of a number
# Factors of 6: 1 2 3 6


print("Factors of a number")
num = int(input("Enter a number: "))
while num > 0:
    print("Factors of ", num, end=": ")
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")
    num = int(input("Enter a number or -1 to quit "))
