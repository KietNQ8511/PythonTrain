myTuple = ("apple", "banana", "cherry")
print(myTuple)

tuple1 = ("e1", )
tuple2 = ("e2")

print(type(tuple1)) # Str
print(type(tuple2)) # Str

# ACCESS
print(myTuple[1])

#    Tuple is unablechange but we can convert tuple to list and handle, then convert it to tuple

# Unpack tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
# green = apple |   yellow = banana |  red = cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *orange) = fruits
print(green)
print(yellow)
print(red) #  "cherry", "strawberry", "raspberry"

# Loop through a tuples
# you can loop through the tuple by using a for loopx

for x in myTuple:
    print(x)

for i in range(len(myTuple)):
    print(thisTuple[i])

i = 0
while i < len(myTuple):
    print(myTuple[i])
    i = i + 1

# Join Tuples
# Join two tuples
# To join two or more tuples you can use the + operator
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# Multiply tuples
# If you want to multiple the ocntent of a tuple a given number of times, you can use the * operator:
# Multiply the fruits tuple by 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2


