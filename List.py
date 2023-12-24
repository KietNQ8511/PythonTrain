""" LIST
- the items have a defined order, and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.
Note: There are some list methods that will change the order, but in general: the order of the items will not change.
Changeable:
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

- A list can contain different data types:
"""

list1 = ["abc", 34, True, 40, "male"]    # <class 'list'>

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1]) # print mango
# The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[2:5]) # print ["cherry", "orange", "kiwi"]
print(thislist[:4]) # print element at pos = 0,1,2,3

# Check if Item Exists
if "apple" in thislist: # return true
    print("true")

""" Change list item
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# change value from 1 to 3
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]  # thay thế p tử thứ 2 và remove element 3   // just apply for Python 3
# Note: // just apply for Python 3
print(thislist)  # print ["apple", "watermelon"]
print(len(thislist))

# Insert an element
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # print : ["apple", "banana", "watermelon" , "cherry"]


