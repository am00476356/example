"""
Comprehension

* writing in line lists, dict.

in-line if else??

x = True_S if condition else False_S
comprehension

enclosed by [] --> list comprehension
variable_name = [True_condition_value_to_be_added for item in iterable if condition]


if **

[true_value for i in iterable if condition]


if else **

[true_value if condition else False_value for i in iterable]


if-else:
 -- if else loop
if
-- loop if


Set comprehension
enclosed within {}

dict[key] = value

k:var
{}
{}
[]
❌() --> not a tuple comprehension --> immutable
strings? immutable


Are dictionaries ordered?

List is ordered, Set is unordered.
Tuple is ordered. Dictionaries?

"""

x = (2, 3, 4, 5, 6, 7, 8)

# WAP to make a new list with numbers which are even
# output = []
# for item in x:
#     if item % 2 == 0:
#         output.append(item)

# output = [item for item in x if item % 2 == 0]
# print(output)


# WAP to form a list of all the numbers to the power 3
# output = [item for item in x]
# print(output)

# WAP to make a list of value marked as even or odd
# ["even", "odd", "even"]

# output = ["odd" if item %2 ==1 else "even" for item in x]
# print(output)

# dictionary
# output = {
#     2: "even",
#     3: "odd",
#     4: "even"
# }

# output = {"even" if item % 2 == 0 else "odd" for item in x}
# print(output)

# output = {item:"even" if item % 2 == 0 else "odd" for item in x}
# print(output)


# output = {item:"odd" for item in x if item%2==1}
# print(output)

# WAP to make a dictionary with value in a list and its datatype as value
# y = ["hello", 3, 4.5, 5+6j]
# output = {item:type(item) for item in y}
# print(output)
