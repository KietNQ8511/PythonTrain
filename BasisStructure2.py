"""Python global variable
Global variable created outside of a function (as in all of the examples above) are known as global variables
"""

# Global variable
x  = "awesome"
def myFunc():
    print("Python is " + x)
myFunc()

# if create a variable same name inside a function
# this variable is local variable

def myFunc():
    x = "fantastic"
    print("Python is " + x)
myFunc()

# The GLOBAL keyword
# can create global variable inside a function
def funcGlobalVar():
    global a
    a = "fantastic"
funcGlobalVar()
print("Python is " + a)

# can also using global keyword to modify value of global variable
def funcModifyGlobalVar():
    global x
    x = "global variable x was modify"
funcModifyGlobalVar()
print(x); # print global variable x was modify
