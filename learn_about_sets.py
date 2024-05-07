"""
set
set contains only unique values inside it, and it is not ordered.

list - buffer space
set -- fixed

representation of sets is {}
to define a set we use set() # creates an empty set

a.difference(b) ==> things present in a but not in b


add --> to add an element
update --> to add unhashable data/sets into set(union)
union

pop --> removes the random element and returns it
discard --> removes the given element but doesn't throw any error if element not present
remove --> removes the given element but throws KeyError if element not present
clear --> set()
"""

# a = set()
# print(type(a))
# a = set()
# a.add(1)
a = set()
a.add(45)
a.add(40)

# x = "google"  # how many alphabets are there?
# y = set(x)
# print(y)

# x = 45
# y = '45'
# string ==> enclosed in quotes
# set --> it is stored in terms (key, value) pair

a = set({1, 2, 3, 4})
print(a)
print(type(a))
b = set({1, 2}) # {7,8}
# print(b.difference(a)) # {}
# print(a.difference(b)) # {3, 4}
b.difference(a) # returns a new set
# print(a.difference_update())

a.remove(2)
a.discard(2) # removes the specific value
a.pop() # randomly removes an element

a.add()
a.update()
a.union(b)
