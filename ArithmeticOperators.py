import math
answer = 7/3
print(answer)

# integer division
answer = 7//3
print(answer)

# modulus
answer = 7 % 3
print(answer)

# candy calculator - example
students = int(input("How many students are in the class?"))
pieces = int(input("how many pieces of candy per student?"))

# calculation for total
total = students * pieces

print('You will need', total, 'pieces of candy.')


num1 = 3 + 5
num2 = '3' + '5'
num3 = int(3.4556465)
num4 = float(5.4)
print(num1)
print(num2)
print(num3)
print(num4)

print("The Answer is: " + str(40 + 2))
print(str(4) + str(2) + ": Life, the universe and everything")
print("PI: " + str(float(3.14159)))
print("PI: " + str(int(3.14159)))
print("Int Division " + str(int(10 / 4)))
print("Int Division " + str(10 // 4))
print("Floating Point Division " + str(10.0 / 4))
print("Type Casting as float " + str(float(10 / 4)))
print("Type Casting as int " + str(int(10.5 / 4)))
print("Mod: " + str(17 % 3))

print("Order of Operations " + str(2 + 5 / 3))
print("Order of Operations  " + str((2 + 5) / 3))
print("Order Matters " + str(int(1.9) + int(1.9)))
print("Order Matters " + str(int(1.9 + 1.9)))
print("Order and Data Type Matter " + str(1.9 + 1.9))
print("Rounding: " + str(round(1.9 + 1.9, 0)))

print(max(2, 5, 3, 7, 9))
print(min(2, 5, 3, 7, 9))
