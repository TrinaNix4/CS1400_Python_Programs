
# ask user for input, cast it as an int, and assigning it to variable 'repeatNum'
repeatNum = int(input('Please enter a 2 digit number: '))

# output
result = repeatNum * (3 * 7 * 13 * 37)
print('Watch it repeat!', result)

print("Let's have some more fun with math!")

# input
num1 = int(input("Enter a number: \n"))
num2 = int(input("Enter another number: "))

# calculations
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print('Division', num1/num2)
print('Int Division', num1//num2)
print('Modulus', num1 % num2)
# once calculated, cast as a string so it can be concatenated with the 'power of' string
print('Power of: ' + str(num1**num2))
