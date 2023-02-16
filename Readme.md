# Lecture Notes

# Variables

- a spot in memory that is holding a value;
- used to hold a value
- assignment

  - = assigns a value to the left hand side
  - variable holds value until assigned again

- name given to variable is an identifier
- rules for identifier naming conventions

  - must start with a letter
  - can use \_ and digits
  - case senstitive
  - keywords that are part of the language cannot be used
  - good practice

    - start with lowercase
    - use camelcase or \_ between words

    good ideas - firstName, first_name
    bad ideas - First Name, 1Name, n, first-name, firstname

    - Data Types
      - in python, the data type if inferred
        - float
        - int
        - string
        - boolean

* a variable is an object
  every object has:

  - value
  - type
  - identity (unique identifier)

* Casting

  - in the program a variable can be cast as a different data type temporarily
  - age = 35
    - cast age as a string
      - print('My age is:' + str(age))
    - cast age as a float
      - float(age)

* doesn't change the data type in memory, just temporarily casts it as a float

# Arithmetic Operators

- Addition + (also concatenation)
- Subtraction -
- Multiplication \*
- Division /
- Integer Division //
- Modulus Division (finds the remainder of the answer) %
- Power of \*\*

# integer division

- a whole number divided by a whole number
- no decimals
  e.g.
- how many groups of 2 can you make with 7 people?
  - 7//2 = 3

# Modulus Division

- given 7 people, if they are divided into groups of two, how many would be left out?
- 7 % 2 = 1 ("7 modulo 2")

# Practice Example

```
#print("The Answer is: " + str(40 + 2))
#print(str(4) + str(2) + ": Life, the universe and everything" )
#print("PI: " + str(float(3.14159)))
#print("PI: " + str(int(3.14159)))
#print("Int Division " + str(int(10 / 4 )))
#print("Int Division " + str(10 // 4))
#print("Floating Point Division " + str(10.0 / 4))
#print("Type Casting as float " + str(float(10 / 4)))
#print("Type Casting as int " + str(int(10.5 / 4 )))
#print("Mod: " + str(17 % 3 ))
#print("Order of Operations " + str(2 + 5 / 3 ))
#print("Order of Operations  " + str(( 2 + 5 ) / 3 ));
print("Order Matters " + str(int( 1.9) + int(1.9 )));
print("Order Matters " + str(int( 1.9 + 1.9 )));
print("Order and Data Type Matter " + str(1.9 + 1.9 ));
print("Rounding: " + str(round(1.9 + 1.9, 0)));

```

**Reflection Questions**

- When do the numbers get added together as opposed to just being put next together in the output?

It depends on what data type the number is. If the number is an int/float, or some type of numerical data type the '+' operator will add them. On the other hand, if it's a string data type, the '+' will concatenate the two numbers. For example
num1 = 3 + 5 will result in 8. It adds the two numbers
num2 = '3' + '5' will result in 35 because it's just concatenating to two strings.

- What happens when you use (int) in front of a number with decimals? How about float?

(int) is a function that will remove anything after the decimal. so the result of >> int(3.1456356) will be 3. If you use float, it turns the number into a decimal (if it's not a decimal already). For example, float(5) gives us 5.0. or float(5.0) gives us 5.0

- Are there any order of operations that are similar to Math? Are there any that are new to you or different from math?

Order of operations are the same as in math PEMDAS, done in order of parenthesis, exponents, mult, division, add, subtract. So 2 + 2 _ 2 would be (2 _ 2) first (the answer is 4), then add that to 2. so 4 + 2 >> the answer is 6.
Casting is new to me. The concept that two strings will be concatenated vs. two numbers that will be added - this threw me off a little when I first saw it, but as I practice with it more, it's becoming clear.

```
#get the input
fahrenheit = float(input("Enter a Temperature in fahrenheit: "))

#do the math
celsius = 5/9 * (fahrenheit - 32)

#display the answer
print(fahrenheit, "is", celsius, " in Celsius")

```

1. Run the program below. Enter the value 32 when it prompts you. Does the program seem to work?

Yes. 2. What are the two variables named?

Farenheit and Celsius 3. Look at the “Get the Input” section. What command allows the program to allow the user to enter something?

The input() function. 4. The variable fahrenheit is going to store what data type?

An int. 5. Run the program again. This time enter the value 50.5. Why do you think it crashes?

The error is gives is: invalid literal for int() with base 10: '50.5'. When I looked this error up on StackOverflow, I learned it means that the string provided (in this case: '50.5') could not be parsed as an integer. The string that asks the user to enter a temperature in farenheit is being cast as an int so it cannot store a number that is a float.

6. Change the cast of the input result so that the variable fahrenheit stores decimals. (Use float instead of int)

If I change the casting from 'int' to 'float' it works as expected.

7. Run the program again. Enter the value 50.5. Did the program crash?

No.

Look at the answer. Is this correct?

No, the answer comes back as 0, but should be 10.28.

8. Look at the “Do the Math” section of the code. Is there anything there that would cause the output to be 0? (Hint: What happens when you have //?)

The '//' is used for floor division which rounds down to the nearest whole number so in this case 5/9 = 0.55 which is being rounded down to 0. So 5 // 9 >> 0 and 5 / 9 = 0.55 9. Fix the error in the code and run the program a few more times to test it out.

Just change the floor division to regular division. 5 // 9 >> 5 / 9.

# Lecture Notes

- Power supply - provided power to different areas of computer
- Main board/motherboard – processing device; printed circuit board; houses peripherals like video card and network card

- Processor - brain of the computer; does all mathematical; sits on the motherboard; the CPU
  Interprets and executes instructions; manages - input, output, and storage devices

- RAM - random access memory; temporary memory; stores data while power on; no longer have access once power is off

- Expansion slots -

- Video card - connects computer to the monitor; circuit board attached to the motherboard

- Network card - a circuit board that connects the computer to the rest of the network usually using special cables

- Hard drive - long term storage; can have SATA vs SSD;

# Hard drive sizes -

- terabyte = 1024 GB;
- GigaByte = 1024 megabytes
- Megabyte = 1024 kilobytes
- Kilobytes = 1024 bytes
- Byte = 8 bits
- Bit = 1 or 0

# Incrementors: Counters

keep track of a value

- add to value
- subtract from value

* = assignment operator that assigns the value of the left side to the value of the right side

# increments operators

=+ add to
-= subtract from
\*= multiply by
/= divide by

- counter or accumulator - any time you are taking a variable and doing something to it and storing it back into itself

# example

- incrementors: Counters
  keep track of a score

```
score = 0
print('Score: ", score)

#wins 1
score = score + 1
print("Score: ", score)

#wins 5
score = score + 5
print("Score: ", score)

#loses 1
score = score - 1
print("Score: ", score)

```

# Operators

- allow us to compare 2 things

* '> greater than'
* < less than
* == compare equal
* != compare not equal
* <= greater than equal
* '> = less than equal'

# if statement

- executes statements if expression is true
- skips statements if expression is false

```
if(force < 10):
  print("Jedi Hopeful")
```

colon and tabs specify what is in the 'if' statement

# Else

- executes when conditions are not true

# Elif: Else if

- runs the first true statement

```
if(force < 10):
  print("Jedi Hopeful")

elif (force < 25):
  print("Jedi Padawan")
elif (force < 50):
  print("Jedi Master")
else:
  print("Jedi Knight")

```

- in above example, if force = 15; it will check the first and skip because not true,
  check the 2nd and print "Jedi Padawan" because it is true and won't bother going on to check the rest.

# Combining Boolean Operators

- Or - returns true if one statement is true
- And - returns true if all statements are true

# And

- both statements must be true to execute

```
import random
die1 = random.randrange(1, 7)
die 2 = random.randrange(1, 7)

if die1 == 1 and die2 == 1:
  print("Snake Eyes!")

```

# Or

only one statement must be true to evaluate to true
