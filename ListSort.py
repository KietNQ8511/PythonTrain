""" SORT LISTS
"""

# Sort method will sort by alphaNumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort reverse
# Sort descending
thislist.sort(reverse = True)
print(thislist)

# Customize Sort function
# https://www.w3schools.com/python/python_lists_sort.asp
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# COPY list
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy() # OR CAN USE    mylist = list(thislist)
print(myList)

# JOIN LISTs
print("=============== JOIN LISTs ===============")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# --------------- #
for x in list2:
  list1.append(x)
print(list1)
# ----------------- #

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# ------------------ #
'''
append()	 Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	       Returns a copy of the list
count()	       Returns the number of elements with the specified value
extend()	  Add the elements of a list (or any iterable), to the end of the current list
index()	       Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	 Removes the item with the specified value
reverse()	  Reverses the order of the list
sort()	         Sorts the list
'''
