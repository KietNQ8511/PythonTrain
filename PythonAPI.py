# ======================================== #
# Boolean
# the value returned in python expression is (True or False) , it upper case first letter
bool("hello") # return True
bool(15) # return True

"""
All string is true except empty string
all number is tue except 0
Any list, tuple, set, and dictionary are True, except empty ones.
"""

print("instance API")
# check an instance have type ????
print(isinstance(1, int))

# if else: Python not use # || , &,
""" guideline
and :
x < 5 and x < 10

or:
x < 5 or x < 4

not:
Reverse the result
not (x < 5 and x < 10) // return true if x < 5
"""

class MyClass():
    def _func1():
        return 0

class1 = MyClass()
class2 = MyClass()

print("____check class____")
print(class1 is not class2)


"""
Python identify Object
is: Returns True if both variable is the same object
"""

"""
is not:
return True if both variable is not the same object
"""
[]a = int[10]

print(a)