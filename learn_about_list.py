"""
Sample program to learn operations on a list

TO-DO list
 - adding tasks
 - completed task remove.
 - reset the TO-DO
 - how many tasks are there to do?

"""
# to_do = []  # currently, to-do is empty
# task1 = "Practice python"
# to_do.append(task1)
# print("The to-do list after adding task1")
# print("to-do ::", to_do)
# task2 = "Submit on thread"
# # to_do.append(task2)
# # priority of task2 is higher so, we need to add it before task1
# to_do.insert(0, task2)
# print("The to-do list after adding task2")
# print("to-do ::", to_do)
# # how many tasks are currently present
# no_of_elements = len(to_do)
# print('tasks in to-do are', no_of_elements, sep=' ')
#
# # if submit on thread i.e. task2 is done:
# # to_do = [task2, task1]
# removed_task = to_do.pop(0)  # to_do.remove(task2)
# print(removed_task, 'task is removed')
# print("to-do ::", to_do)
# # reset the to-do
# to_do.clear()
# print("to-do after reset ::", to_do)


# what can be added elements which can be of any datatype

# all_to_dos = [pal_to_do, shreya_to_do, anuj_to_do] # add list into a list


# I have a list of numbers find the smallest and largest
# a = [65, 89, 96, 55, 102, 55]


# a = []
# buffer space for list --> values add increases --> buffer increases

"""
basic indexing

a = [2, 5, 7, 1, 3, 4]
indexes = 0, 1, 2, 3, 4, 5
==== -6, -5, -4, -3, -2, -1
a[index] --> 1 value at the index position

slicing:
from index to last index
a[from_index:last_index, step_value=1] -->
default values ::
from_index=0
last_index=len()
step_value=1

*** from_index is included while last index is excluded

strings
list
"""
# a = "londoncityincanada"
# b = a[::]
# print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = a[2::3]  # 3, 6, 9
b = a[1::3]  # 2, 5, 8

c = ['ahmedabad', 'gandhinagar', 'valsad', 'vadodara', 'amalsad', 'surat', 'rajkot', 'bhavnagar', 'junagarh']
# c.sort() # default sorting for list of strings is by alphabetical order
# requirement is to sort by length
# c.sort(key=len)
# c.sort(key=len, reverse=True)
# print(c)

a = list()  # this also creates an empty list
