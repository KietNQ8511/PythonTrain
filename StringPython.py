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