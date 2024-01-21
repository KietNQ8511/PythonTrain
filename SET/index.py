thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)

tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)
print(thisSet)

# Add any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, list, dictionaries etc, ...)

# Remove set items, remove item
# To remove an item in a set, use the remove(), or the discard() method
#remove "banana" by using remove method
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")
print(thisSet)

thisSet = {"apple", "banana", "cherry"}
thisSet.discard("banana")
print(thisSet)
"""
You can also use the pop() method to remove an item,
but this method will remove a rangom item,
so you can not be sure what item that gets removed
"""

# We can use method CLEAR and DEL with SET
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Python - Join sets
# The union() method returns a new set with all items from both sets:
set1.union(set2)

# The update() method inserts the items in set2 into set1:
set1.update(set2)
# Keep ONLY the Duplicates
set1.intersection_update(set2)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
z = set1.intersection(set2)
print(set1)
# Keep All, But NOT the Duplicates
set1.symmetric_difference_update(y)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
# Return a set that contains all items from both sets, except items that are present in both:
set3 = set1.symmetric_difference(set2)
