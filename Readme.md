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

# Binary Search Tree

- each node has at most 2 child nodes, referred to as the left child and right child.

- the value of the left child is always less than the value of the parent node

- value of the right child is always more than the value of the parent node

- each node contains a value, a left child node, and a right child node

- topmost node called the root node;

- efficient search,insertion, deletion operations if it's a balanced tree

- used to represent ordered data like in phone books, dictionaries, and file systems

# Hash Table

- used to store and retrieve data quickly and efficiently
- can find data immediately
- collection of key-value pairs where each key is unique and corresponds to a value

- key is used to calculate a hash code, which is used to index into an array to find the corresponding value

- implemented using a hash function - which take the key as input and generates a hash code, which is an integer that is used to index into the array; value is then stored at that index in the array; if the key is not found, the hash function is used to calculate a new index until the key is found or all possible indices have been checked

- what is hashing?

* gives a method to find items immediately e.g. using abingo card to find N44; hashing stores the data using an algorithm (hash function) and retrieves the data using the same hash function

- what is modulus division?

* ususally used to create the algorithm for a hash table;
* finding the remainder of a division problem e.g. 15 % 4 = 3

- e.g. where would the following data be stored in hashtable using the hash function n%7?
  data: 40, 14, 24, 11, 20

- 40/7 = r5
- 14/7 = 2 r0 and so on..
- 0 -14
- 1
- 2
- 3 - 24
- 4 - 11
- 5 - 40
- 6 - 20

# Built-in Methods

- functions and types that are always available

* Round

- rounds up or down;

```
num = 123.4567
num = round(num, 2)
print(num)

```

- Min Max

* returns the min or max value

```


```

- also works with text - alphabetically arranging strings

- math.ceil(x) - returns the next smallest integer
- math.floor(x) - returns the previous smallest integer
- math.pow(x, y) returns x to the power of y
- math.sqrt(x) - returns the square root of a number
- math.isqrt(x) - return the square root integer
- math.abs(x) - returns the postive integer
- math.fabs(x) - returns the absolute value

- math.max(x, y, ...) - returns the largest value
- math.min(x, y, ...) - returns the smallest value

# Math library Usage

- must import math to use these functions

```
import math

num = 9
print(math.pow(num, 3))

```

# Random library

- import random
- generates pseudo-random numbers

```
import random

num = random.randrange(1, 5)
print(num)

```

# Strings are a list

```
letters = "ABCDEFG"
print(letters[1])

```

=> B ; we start counting at 0

```
print (letter[3:6]) prints starting at 3, but not including 6
=> D E F
```

# Strings Length

```
word = input("Enter a word: ")
wordLen = len(word)
print(word, "is", wordLen, "letter long")

```

=> Enter a word: Happy
Happy is 5 letters long

# Multi line string

if you want to do a multi line string or embed quotes inside of a string

use triple quotes to start and end string

```

txt = """She said, "Knock knock?" He replied, "Who's There?" """
print(txt)

```

=> She said, "Knock knock?"
He replied, "Who's there?"

# Strings Case

```
word = input("Enter a word: ")
print("Upper Case:", word.upper())
print("Lower Case", word.lower())

```

=> Enter a word: Perpendicular
Upper Case: PERPENDICULAR
Lower Case: perpendicular

# String find

- returns the position of whatever it is you're looking for

```
txt = "Come and clean the chaos in your closet"
pos = txt.find("c")
print(pos)

```

=> 9

- case sensitive and counts spaces as 1

If you want to find the 2nd instance: add one to variable; start search at char 10

```
txt = "Come and clean the chaos in your closet"
pos = txt.find("c")
print(pos)

#start search at char 10 (cause pos is char 9 from code above)
pos = pos + 1
pos = txt.find("c", pos)
print(pos)

```

# String replace

- finds any instances of c, and replaces it with k. case sensitive

```

txt = "Come and clean the chaos in your closet"
print(txt.replace("c", "k"))

```

=> Come and klean the khaos in your kloset

- these functions returnsa value. doesn't modify the text itself, just return something

- if we use an = sign to assign whatever is returned, this will modify it

```
txt = "Hello Trina"
txt.replace("e", "a")
print(txt)
```

=> Hello Trina
vs.

```
txt = "Hello Trina"
txt = txt.replace("e", "a")
print(txt)

```

=> Hallo Trina

```
txt = txt.upper()
print(txt)

```

=> HALLO TRINA

# Slicing strings

- doesn't modify original text

```
txt = "ABCDEFG"
print(txt[1: 3]) //up to but not including 3.

```

=> BC (1 and 2 )

# Slice from the beginning

```
txt = "ABCDEFG"
print(txt[:3])
```

=> ABC

# Strip: Remove whitespace

- removes any extra spaces

```
txt = "     A     "
txt = txt.strip()
print(txt, "END:)

```

=> A END

# Concatenating

```
txt1 = "ABC"
txt2 = "DEF"
txt3 = txt1 + txt2
print(txt3)

```

=> ABCDEF

# Concatenating Numbers

```
txt = "ABC"
num = 42
final = txt + num
print(final)

```

=> ABC42

# Lists

- store multiple items in a single variable
- use square brackets to identify it

```
mylist = ["apple", "banana", "cherry"]
print(mylist)

```

=> ["apple", "banana", "cherry"]

can include integers, floats, or a mixed list of all

# length function

- can use len to determine the number of items in a list

```
mylist = ["apple", "banana", "cherry"]
print(len(mylist))

```

=> 3

# accessing a single item in a list

```
mylist = ["apple", "banana", "cherry"]
print(mylist[1])

```

=> banana

# changing a value in a list

- square brackets can change a value

  ```
  mylist = ["apple", "banana", "cherry"]
  mylist[2] = "zucchini"
  mylist[0] = "yam"
  print(mylist)
  ```

=> ['yam', 'banana', 'zucchini']

# adding/appending a list

- append allows you to add to a list

```
  mylist = ["apple", "banana", "cherry"]
mylist.append("dragonfruit")
print(mylist)


```

=> ['apple', 'banana', 'cherry', 'dragonfruit']

# declaring an empty list

- you can start with an empty list

```
mylist = []

mylist.append("dragonfruit")
print(mylist)

```

=> ['dragonfruit']

# Inserting

- append always appends to the end
- insert allows you to specify where you want to add the item
- adjusts the index of the rest of the list

```
  mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "apricot")
print(mylist)

```

=> ['apple', 'apricot', 'banana', 'cherry']

# removing by item

- allows you to remove from the list

```
  mylist = ["apple", "banana", "cherry"]
mylist.remove("cherry")
print(mylist)

```

=> ['apple', 'banana', 'dragonfruit']

# removing by index

- pop allows you to remove a particular position

```
  mylist = ["apple", "banana", "cherry", "dragonfruit"]
  mylist.pop(3)
  print(mylist)

  intlist = [2, 4, 6, 8]
  intlist.pop(2)
  print(intlist)

```

['apple', 'banana', 'cherry']
[2, 4, 8]

# removing a last item

- pop allows you to remove a particular position; if not specified then it removes at the end

# clear

- clears the entire list of contents

```
    mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)

```

=> []

# iterate a list

- use a loop to access each item in the list

```
  mylist = ["apple", "banana", "cherry"]
for x in mylist:
  print(x)

```

apple
banana
cherry

# iterate a list

- the only way to actually change the value is to use the square brackets

```
  mylist = ["apple", "banana", "cherry"]
  for x in mylist:
      x = "zucchini"
  print(mylist)

```

apple
banana
cherry

# iterate by index

- use a loop to access each item in the list

```
mylist = ["apple", "banana", "cherry"]

for i in range(len(mylist))
  print(mylist[i])

```

apple
banana
cherry

- now to change the list, can use square brackets in the same type of list as above

```
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist))
  mylist[i] = "zucchini"
print(mylist)

```

=> ['zucchini', 'zucchini', 'zucchini']

# add 1 to each item in the list

```
mylist = [ 1, 2, 3, 4, 5]
for i in range (len(mylist))
mylist[i] = mylist[i] + 1
print (mylist)

```

[2, 3, 4, 5, 6]

# Counters

- variables that keeps getting added to

```
data = [13, 12, 18, 11]
sum = 0
for i in range(len(data)):
  sum += data[i]
print(sum)

```

=> 54

- have a for loop that iterates through the array then have some sort of variable that performs a calculation on every element in the array

# Sorting word lists

- putting the values in order; sort alphanumerically

```
mylist = ['elderberry', 'apple', 'dragonfruit', 'cherry', 'banana']
mylist.sort()
print(mylist)

```

=> ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']

# sorting number lists

- putting the values in order

```
intlist = [6, 3, 5, 2, 9]
intlist.sort(reverse = True);
print(intlist)

```

=> [9, 6, 5, 3, 2]

# list comprehension

- shorter syntax for creating a new list

- long way

```
lst = []
for i in range(10):
  lst.append(i)

```

=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

- short way

```
lst = [i for i in range(10)]

```

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

```
allPeople = [["Kim", 21]], ["Rosie", 7], ["Frank", 66]]
adults = [x for x in allPeople if x[1] > 20]

```

[['kim', 21], ['frank', 66]]

# Tuple

- stores multiple items in a variable
- unchangeable, cannot add or remove
- ordered: defined order that cannot change
- round brackets

```
mylist = ('apple', 'banana', 'cherry')
print(mylist)

```

# unpacking tuples

unpacks the tuple into individual variables

```
contact = ('smith', 'jane', '123 fake street', 'ogden', 'ut', '84405')
lname, fname, adrss, city, state, zip, = contact
print(state)

```

=> UT

```
contact = ('smith', 'jane', '123 fake street', 'ogden', 'ut', '84405')
lname, fname, *adrss = contact
print(adrss)

```

=> ['123 fake street', 'ogden', 'ut', '84405']

# Dictionary

- stores data with a key. they key is paired with the value
- no duplicate keys
- duplicate values are allowed

- use curly brackets
  colon seperate key-value pairs

```
myDict = {'red': 'apple', 2: 'banana', 3: 'cantaloupe'}
print(myDict)

```

=> {1: 'apple', 2: 'banana', 3: 'cantaloupe'}

# Length

- the difference between a list and a dictionary is when you find len, it tells you how many key,value pairs there are

# Accessing a single item

- use the key as an index

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
print(myDict['red'])
print(myDict['orange'])

```

=> apple
=> cantaloupe

# changing a value

- the key can adda value

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
myDict["blue"] = "blueberry"
print(myDict)
```

{'red': 'apple', 'yellow': 'banana', 'orange':'cantaloupe', 'blue':'blueberry'}

# udpate a value

-cannot have duplicate values so it will just replace whatever is there, or update it

# Declaring an empy dictionary

- you can start with an empty list using dict()

```
myDict = dict()
myDict["red"] = "Apple"
myDict["yellow"] = "banana"
```

# removing an item

- Pop() allows you to remove from the list by key;
- removes the last one if you don't specify

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
myDict.pop("red")
print(myDict)
```

=> {'yellow': 'banana', 'orange': 'cantaloupe'}

# deleting all items

- clear method allows you to remove all items

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
myDict.clear()
print(myDict)
```

=> {}

# iterate the keys

- keys returns the keys

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
for x in myDict.keys():
  print(x)

```

=> red
yellow
orange

# iterate by values

- use a loop to access each item in the list

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
for x in myDict.values():
  print(x)

```

=> apple
banana
cherry

# iterate both

- items access the dictionary items

myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
for k, v in myDict.items():
print(k,v)

=> red apple
yellow banana
orange cantaloupe

# shallow copy

- shallow copy uses = operator; it's a literal copy. 2 different names for the same item so what is done to one item will be done to the other

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
fruit = myDict
fruit.pop('red')
print(myDict)
print(fruit)

```

=> {'yellow': 'banana', 'orange':'cantaloupe'}
=> {'yellow': 'banana', 'orange':'cantaloupe'}

# deep copy

- uses the copy() function; creates an actual physical copy so 2 different lists with 2 different names

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}
fruit = myDict.copy()
fruit.pop('red')
print(myDict)
print(fruit)

```

=> {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}

=> {'yellow': 'banana', 'orange':'cantaloupe'}

# Search

- use in, or not in to determine if a key exists

```
myDict = {'red': 'apple', 'yellow': 'banana', 'orange': 'cantaloupe'}

if 'red' in myDict:
  print("Red is a key")

if 'blue' not in myDict:
  print('Blue is not a key')

```

=> Red is a key
=> Blue is not a key

# Zip

- Combines 2 lists into one dictionary

```
days = ["sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

weekly_temp = {day:temp for (day,temp) in zip(days, temp_C)}
print(weekly_temp)

```

{'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday':29.8, 'Friday':30.2, 'Saturday': 29.9}

- the following code segment will count how many times each word occurs in the given text

```
text = "one fish two fish red fish blue fish black fish blue fish old fish new fish"

lst = text.split()
wrdList = dict()
print(lst)

for x in lst:
    if x not in wrdList:
        wrdList[x] = 1
    else:
        wrdList[x] += 1

for i in wrdList:
    print (i, wrdList[i])
```

['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'black', 'fish', 'blue', 'fish', 'old', 'fish', 'new', 'fish']
one 1
fish 8
two 1
red 1
blue 2
black 1
old 1
new 1

```
shelterAnimals = {"dog": 49, "cat": 38, "bunny": 14}
originalShelter = shelterAnimals.copy()
shelterAnimals['dog'] += 2
shelterAnimals["ferret"] = 2
shelterAnimals["cat"] -= 3
shelterAnimals["snake"] = 4

if shelterAnimals['dog'] > 50:
  print("Shelter full.")
if 'rat' not in shelterAnimals:
  print("No rats.")
print(shelterAnimals)
print(originalShelter)
```

Shelter full.
No rats.
{'dog': 51, 'cat': 35, 'bunny': 14, 'ferret': 2, 'snake': 4}
{'dog': 49, 'cat': 38, 'bunny': 14}

# Try and except

# Exception Handling

- want to make robust code that handles errors it encounters
- run time errors - crashes entire program with no recovery
- exception handling
  - errors during execution
- use a try/except to help with dangerous code
- allows for continued execution

```
try:
#excecute code that could be dangerous
except:
#what happens if exception is encountered.
```

- try block encountered
- error encountered, except block executed
  - any lines of code after exception in try are skipped
- if no errors, except block skipped
- program continues as normal after try and except block executed

e.g.

```
try:
#dangerous code
age = input("What is your age?")
#causes an error if you type the word 'twenty'
int(age) \* 10
except:
#handle the error so the program doesn't crash
#print a message
print("invalid input")
```

# Raising Exceptions

- if we want to force an exception to happen that usually doesn't cause an error

- format:

```
try:
#dangerous code
age = input("What is your age?")
#won't cause an error if enter -5, but we want it to throw an error because -5 is not a real age
int(age) \* 10
 if age <= 0:
  raise ValueError('Invalid age')

except ValueError as except:
#handle the error so the program doesn't crash
#print the message passed when the error was raised
print(except)
```

# Reading from files

- common task in programming is to read info from a file
- steps:
  - open the file
  - read from the file
  - close the file

```
# open function, file name, mode -r for read
f = open('txtFile.txt', 'r')

lines = f.read()
f.close()

```

# sequential access vs random access

- sequential - files are read sequentially

- random access - go directly to a spot within the file

to read one line at a time insetad of reading the entire file we can use:

- .readline()

- tracks which line it is on

```
f = open('textFile.txt', 'r')
line1 = f.readline()
line2 = f.readline()
f.close()

```

- above could be inefficient if there are a lot of lines to read so we can use a for loop to read each line in the file

```
f = open('textFile.txt', 'r')

for line in f:
 print(line)

f.close()

```

- reading into a list - may want to keep the info instead of storing it temporarily. in case we want to manipulate it

```
myList = []

f= open('textFile.txt', 'r')

for line in f:
  # strip off new line character
  line = line.strip()
  # add to list
  myList.append(line)

f.close()

```

# writing files

- we can use a file to store data; bigger companies may use a database

- steps:

  - open the file
  - write to the file
  - close the file

  ```
  #open function, file name, mode -w for write
  f = open('textFile.txt', 'w')

  f.write('purple\n')
  f.write('orange\n')
  f.close()

  ```

- write to a file from a list

```
# have a list of colors
colors = [purple, orange, yellow]
# open the file to write
f = open('textFile.txt', 'w')

#use for loop to write to the file and write each of the colors to a new line using \n to ensure each color is on its own line
for c in colors:
  #write to file
  f.write(c + '\n')

  f.close()

```

# Using exceptions with Files

- common modes and common errors associated with them

* 'r'

  - open file for reading. if file doesn't exist, exception is thrown

  * 'w'

  - open file for writing. if file does not exist then file is created. contents of an existing file are overwritten

  * 'a'

  - open the file for appending. if file does not exist then the file is created. writes are added to end of existing file contents

  * - can be added to the end of a mode which allows for both reading and writing

- an exception occurs if file is not found
- use a try when working with files

```
try:
# open the file - if it does not exist it will cause an exception
  myFile = open('myData.txt', 'r')
except FileNotFoundError as err:
  print(err)
```

# User-defined functions
 
 - programs may repeat code causing unecessary redundancy
 - creating a function can eliminate this
 - function: 
  - grouping of statements with a common purpose
  - helps address a specific task 
  - for example:
    - calcuations
    - rolling die
    - printing an output 

* functions - named series of statements
function definition - the actual name of the function and the statements contained within it

* def - the keyword used to create a new function

* function call - (calc_area()) - an invocation of the functions name this means the function will get executed 

* if the function is never called, the statements would never be ran 



* parameter - input the function takes specified in the function definition e.g. def sum_nums(num1, num2)

* python has dynamic typing - don't have to specify what type of parameters are as you might have to in other languages which are static typing

* in dynamic. the same function could represent an int and a string

# why functions? 
- readability
- modular development -  
- avoid redundancy

# function are objects
 - can be passed as arguments

 # object scope

  - variables created inside the function are only available within the function
    - local variables

  - variable defined outside of a function- accessible to every function and the main program
    - global variable


e.g name and number declared inside the function so not accessible outisde of function (in the print statement)
```
def assign_player_number():
  name = input("what is your name?")
  number = input('what is your number?')
# return the name and number

#main program
assign_player_number()

print(name, number)
```

# can use keyword 'global' to specify that we are referring to the global variable and not a local variable 
```
team_name - 'rockies'

def assign_player_number():
  global team_name
  team_name - input('what is the team's name?')
  name = input('what is the player's name?')
  number = input("what is the player's number?')
  print (team_name, name, number)

  #main program
  assign_player_number()
  print(team_name)
  ```
- will result in changing the global variable to user input

# Classes

- a function is one very specific task
- a class is a group of those tasks and attributes that are related to one another

- in the real world we think about things on higher level and we group items together 
  - instead of metals, woods, and fibers that make up an item, we group those items together as cars, hotels, or restaurants on a higher level 

- blueprint for what it may become
- specifics are not set but it gives an outline for those items

- university -> weber state
university is the class and weber state is an instance of the class
- car -> nissan
- planet -> saturn 

- class object and we can create copies or isntances of that object
- restaurant class and we can break it down into smaller tasks or attributes

- we can pull in the 'restaurant' class and not have to pay attention to all the lower level details - they are hidden  i.e.  making a reservation at a restaurant 

- this is called abstraction - user is interacting at a higher level and not having to deal with all the internal lower level 

to use a class: 
class keyword - create an object type containing groups of related variables and functions 

```
class Calendar: 
  def ...

  ```

  # instantiation

  - calling the class similar to calling a function "instantiate a class" 

  my_calendar = Calendar()

  * classes are upper case so we can easily differentiate when reading the code 

  - creates an instance of the class which exists as an object in memory

  * when an instance is created the _init_ method is automatically ran 
    - similar to a constructor in other languages
    - allows for defaults to be set or setting the initial state of the instance
    - functions inside a class are referred to as methods
    - the _init_method has a parameter "self" which references teh isntance created 

    - dot notation is used to reference the attributes of the class

    * instance and instantiation 
    ```
    myCalendar = Calendar() (instantiated)

    ```

    myCalendar is an instance - an individual object - myCalendar now refers to an instance of the Calendar class  
    - all the code contained within the Calendar() class is now held within myCalendar in memory

    - instantiation - calling the class
    - instantiation calls the init method automatically

    ```
    class Calendar:
      def __init__(self):
        self.name_of_month = "NotSetYet"
        self.days_in_month = 0 
    
    myCalendar(Calendar())
    print(myCalendar.name_of_month)

    ```

    - dot notation - access attributes within the class

    - functions within a class are known as instance methods

    - __init__ is also a method but it is a special method __ identify special methods that have defined behaviors 

    ```

    class Calendar:

      def __init__(self):
        self.name_of_month = "NotSetYet'
        self.days_in_month = 0 

        # instance method/function (user defined)
      def print_month_info(self):
        print(self.name_of_month)
        print(self.days_in_month)

    myCalendar = Calendar()
    myCalendar.name_of_month = 'January'
    myCalendar.days_in_month = 31
    myCalendar.print_month_info()

    ```

* the parameter of self is a reference to the instance of the class; self is bound to myCalendar. the method's code can use self to access the instance attributes or other methods 




