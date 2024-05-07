"""
WAP to traverse through a string in reversed order.
"""
name = 'Hello'
# for char in name[::-1]:
#     print(char)

# for idx in range(len(name)-1, -1, -1):
#     print(name[idx])

# for char in reversed(name):
#     print(char)


"""
WAP to count the number of characters present in the given string without using len function.
"""
count = 0
for char in name: # H e l l o
    count += 1

# print(count)


"""
print the index and value of each element in a list.
a = [55, 66, 77, 88]
(0, 55)
(1, 66)
(2, 77)
(3, 88)
"""
a = [55, 66, 77, 88]

# for idx in range(len(a)):
#     print(idx, a[idx])

# for item in a:
#     print(a.index(item), item)
#
for seq, item in enumerate(a):  #--> returns  (idx, item)
    print(seq, item)