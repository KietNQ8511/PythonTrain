""" List Comprehension
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x  in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension
# get element have symbol "a" in the list append to newlist
newlist = [x for x in fruits if "a" in x] # list have elements contains symbol "a"
listUnApple = [x for x in fruits if x != "apple"]

# If no condition:
listNoCondition = [x for x in fruits]

listRange0_9 =  [x for x in range(10)]
print(listRange0_9)# print 0-9

# Same above but add condition < 5
llistRange0_4 = [x for x in  range(10) if x < 5]
print(llistRange0_4) # print 0-4

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist) # print all element as uppercase

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist) # print all element as "hello"

# The expression can also contain conditions, not like a filter, but a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
