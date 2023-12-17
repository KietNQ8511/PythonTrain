"""Variables
    Pyton has no command for declaring a variable.
    A variable is creaed the moment you first assign a value to it.
    A variable name can only contain alpha-numeric characters and underscores (A-a, 0-9, and _ )
    A variable name can not start with a number
"""

# declare a variable (no need data type keyword in the first)
x = 5;  y = "yorn"
print(x) # x is of type int
print(y) # y is of type String

# casting
x = str(3) # x will be '3' -- this is initial and specify the data type of  avariable, this can be done with casting

# Get the type of variable
print(type(y)) # print <type 'str'>

# String double brackets "kiet" = 'kiet'

# Many value to multiple value
x, y, z = "Orange", "Banana",  "Cherry"
print(x); print(y); print(z)

# Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x); print(y); print(z);

x = "Python"
y = "is"
z = "awesome"

print(x, y, z) # print ('Python', 'is', 'awesome')
print(x + y + z) # print Pythonisawesome

x = 5
y = "John"
print(x, y) # print (5, 'John')
