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

Decimal Base 10

1's place - 10^0 - 1
10's place - 10^1 - 10
100's place - 10^2 - 100

# Binary Numbers

1011 0011

- bit - binary digit
- byte: a group of 8 bits
- 1 character - 1 byte of information

1 - 128
0 - 64
1 - 32
1 - 16
0 - 8
0 - 4
1 - 2
1 - 1

find the 1's in the binary number and add them
so: 128 + 32 + 16 + 2 + 1 = 179

- example
  01011011
  0 - 128
  1 - 64
  0 - 32
  1 - 16
  1 - 8
  0 - 4
  1 - 2
  1 - 1

64 + 16 + 8 + 2 + 1 = 91

- can drop 0's on the left hand side

* example 2
  given 37:
  128 - 0
  64 - 0
  32 - 1 so at this point subtract 32 from given number(37) which equals 5; now compare this with place value
  16 - 0
  8 - 0
  4 - 1 -> so 5 - 4 = 1
  2 - 0
  1 - 1 (if number is larger then 1, made a mistake)

* put a 0 if the given number is smaller than the place value
* put a 1 if it's larger or equal

# Convert to Binary

given 29:
128 - 0
64 - 0
32 - 0
16 - 1 subtract 16 from given number (29)= 13
8 - 1 subtract 8 from 13 = 5
4 - 1 subtract 4 from 5 = 1
2 - 0
1 - 1

- answer = 0001 1101

* Binary - literal representation of how data is stored on a computer

* Hexadecimal Base 16
  given the number 5C in hex, what is the number in decimal?

base 16 is:
16^0 - 1
16^1 = 16
(5 \* 16) + C = (80) + 12 = 92

# Hex to decimal

give 2B in hex, convert to decimal
(2 \* 16) + B = 32 + 11 = 43

2B = 43

# convert decimal to hex:

given 58:

58 / 16 = 3 r 10
so 3A

# Binary to Hex

0 - 8
0 - 4
1 - 2
1 - 1

so 3

1 - 8
0 - 4
1 - 2
1 - 1

3B

# Hex to Binary

ED:

split into 2 digits and cnovert separately

E = 14
8 1 (14 is greater than 8) 14-8=6
4 1 (6 is greater than 4) 6 - 4 = 2
2 1 (2 is equal to 2) 2-2=0
1 0 (0 is smaller than 1 )

D = 13
8 1 (13 is greater than 8) 13-8 = 5
4 1 (5 is greater than 4) 5 - 4 = 1
2 0 (1 is less than 2)
1 1
`1110 1101 = ED

# Adding in Binary

# ASCII Code

- code for representing characters on a keyboard
- American Standard Code for Information Interchange

all the characters are one byte of info so h-e-l-l-o in a .txt file would be 5 bytes in size

# Images

- Pixel - picture element; basic unit of color on a computer display

each pixel has a value -

# RGB Color Code

red gree blue (RGB)
each color is a number between 0-255
represents how much of each color
RGB (255, 255, 255) = FFFFFF (FF(red), FF(green), FF(blue))

3 bytes of infomation to make up the color code per pixel; (ff, 00, 00) (red)

# Zipped Folders

- combines files and folders into a single finle
- compresses the information

# Sound representation

sound is variations of pressure in a medium
represented with waves

higher the sound wave - the louder

sampled sound wave - when digitizing the information, losing a little bit of original sound wave because storing it in 1's and 0's.

# Loops

- repeat segments of code
  - for loop: iterates a certain number of times
  - while loop: iterates while a condition is true

# For loop

- use when you know the number of iterations
- negative value for the change when you want to count backwards

```
for i in range(2, 12, 3)
  print(i)

for i in range(5, 1, -1)
  print(i)

```

- above code will start at 2, go up to but not including 12, then count by 3's.
  and
  the 2nd one will print out '5, 4, 3, 2' stops short of 1 because it doesn't include the number

# While Loop

- iterates while a condition is true

```
num = int(input("Enter a number greater than 10"))
while num <= 10:
  num = int(input("Enter a number that is greater than 10"))
print(num, "is greater than 10")

```

# Array

- What is an array?

* Simplest form of data structure. An array is basically just a list. The items in an array are stored right next to each other in memory.

- Given a list size 5, what is the upper and lower bound of that list?

* We start counting at 0 so the lower bound is 0. Upper bound is at 4.

- What value is used to access each position in the list?

* The index value can be used to access the items in the list. So fruit[2] = “mango”, finds the value in position 2 and assigns it “mango”.

- Give an example of something that could be implemented with a 2d array.

* Something that has rows and columns, for example, tic-tac-toe. Could create an array with 2 sets of brackets to indicate rows vs columns. For example, data = [ [2, 3, 3, 4], [4,7,3,8], [7,9,5,0] ]

# Linked List

- What is a Linked List?

* Non-contiguous memory locations.

- What are the elements of a linked list called?

* Node

- What are the two parts to a node?

* Stores the data to be stored and the memory location of the next node, which is storing the next piece of data in the list, and the memory location of the next one, and so on until the last item in the list, which has NULL for the memory location.

- What are some advantages of using a linked list?

* Very easy to add information to the list by just changing the pointers - set the pointer of the new Node to the following location, and set the pointer of the previous node to the new node. Also easy to remove nodes. Has a dynamic size. Small pieces throughout memory.

# Trees

- What is a tree structure?

* Have a root node, and the root node might have links to several different places. It’s a hierarchical structure with a root, nodes, and children. For example, in a windows computer when you look at your stored files. C: drive opens up to all the folders within that drive, then the folders allow access to more folders within those.

- What is a binary tree?

* Every parent only has a maximum of 2 children. To search for a value, start at root, if value is bigger, go to the right. If it’s smaller, go to the left. Keep repeating this until you find the value. This is more efficient compared to a linked list where you just start at the beginning of the list and go through every value.

  - Assume that the following values are to be added to a binary tree. What would the tree look like?

  * Click on the image to select it, then click “Edit” to change the text in the image. Data: 67, 10, 34, 8, 11, 44, 74, 94, 99, 70, 68

# Array

- a collection of elements, where each element is id'ed by an index.

- elements are stored in contiguous memory locations, making it easy to access them; stored right next to each other in memory

- data can be accessed using an index; e.g. fruit[2]="mango" finds the value in position 2 and assigns it 'mango'

- advantages

  - constant-time access to any element in the array
  - efficient insertion and deletion if elements are added at the beginning and end of the array

  * disadvantages
    - have a fixed size;

* if given a list size of 5:
  - upper bound is 4
  - lower bound is 0

# Stack

- linear data structure of elements in which operations are performed in a last-in, first-out (LIFO)

- elements are stored in a stack, which is a list with 2 main operations, push and pop

- push() adds an element to the top of the stack
- pop() removes the element from the top of the stack
- a single pointer that keeps track of the top of the stack

- last element to be added to the stack is the first to be removed

# Queue

- linear data structure

- FIFO - first-in, first out; elements stored in a queue with 2 main functions

  - enqueue - add items to back of queue
  - dequeue - remove from the front of the queue

- first element to be added is the first to be removed, and last element to be added is the last to be removed

- good for tasks that must be processed in order

# Linked list

- linear data structure in which each element, or node, contains a value and a pointer to the next node in the list. The last node points to a null value to indicate the end of the list

- advantages
  - dynamic in size; nodes can be added or removed from the list at any time; small pieces of memory instead of one big chunk of data like an array has.
  - ideal for situations where the size of the data is not known in advance, or size of data may change frequently (adding or deleting data)

* efficient insertion and deletion operations; just change the pointers
* disadvantages - slower random access time than arrays to access a node at a specific index
* require additional memory for storing the pointers

# Tree

- a heirarchical structure consisting of nodes - a root node, and the root node might have links to several different places.

- heirarchical structure with a root, nodes, and children.

- each node may have zero or more child nodes and except for the root node, each node has exactly one parent node.

- root node is the topmost and has no parent;

e.g. file systems on a computer
