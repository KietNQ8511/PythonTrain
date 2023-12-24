"""String in Python
    - String in python are surrounded by either single quotation marks, or double quotation marks.
    'Hello' is the same as 'hello'
    - You can display a string literal with the print() function:
"""
# Multiple Strings using """ || '''
a = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String are arrays
a = "Hello, world"
print(a[1]) # print: e

# Looping through a String
# Since strings are arrays, we can looopj through the characters in a string, with a for loop
for x in "banana":
    print(x) # print each symbol in each line

# String length
print(len(a))

# check a string is subString in another string
txt = "The best things in life are free!"
print("free" in txt) # print : True

# Use it in If statement
if "free" in txt:            # can using "not in" keyword , it oposite with "in" keyword
    print("Yes, 'free' is present.")

""" SLICING
"""
b = "Hello world"
print(b[2:5])   # print :  llo
print(b[:5])     # print : Hello
print(b[2:])     # print : llo world
print(b[-5:-2]) # can print negative: print : wor

""" Function in String python:
 lower() - lower case
 strip() - same trim() in Javascript
 replace(x, y) - replace x -> y
 split(x) - split to an array each element seperate by x
 use + operator to concatenate
"""
string = "Hello, world"
listA = string.split(",")

# Format
age  = 23
txt = "my name kiet , I'm {} years old {} __ {}"
txt = "my name kiet , I'm {2} years old {0} __ {1}" # Can set position of param
print(txt.format(age, 13, 26))

"""
capitalize() convert the first character to upper case
casefold() convert string to lower case
center() return a center a string
count() return the number of times a specified value occurs in a string
"""

