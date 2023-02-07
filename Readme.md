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
