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
myList = thisList.copy()
print(myList)

