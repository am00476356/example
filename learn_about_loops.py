"""
loop?
same action repeated n number of times.

music 🔁

loop -->
use case of loop:

1. to do the same action n number of times.

2. iteration - traversal among the elements
[1, 2, 3, 4, 5]

for i in [1, 2, 3, 4, 5]:
    print(i)

for elem_name in iterable:
    statement for repetition

range
range(5)
range(stop)
start = 0
step = 1
0, 1, 2, 3, 4

range(a, b)
range(start, stop)
a, ... b-1
range(3, 7)
3, 4, 5, 6

range(start, stop, step)
start inclusive
stop exclusive
step difference from start


while condition:
    statement
    .
    .
    .
    statement
    vary for variable in condition
while - keyword
condition - boolean ==> bool(statement)
    statement - block of code

When I am sure about the start and end --> for loop
When I am unsure about the start , I know the end --> while

MALWARE --> something that is intended to corrupt your system

Loop Control Statements
pass - no action [syntax fulfill]

break - stop the execution, and get out of the loop

continue - stop the iteration but carry on with next iteration


for .....:
    statement
else:
    statement2
"""
a = [5, 7, 9, 11]
# for elem in a:
#     print(elem)

# WAP to square each number in the list

# square_me = [1, 2, 3, 4]
# for i in square_me:
#     print(i*i)


# WAP to print a given statement 5 times:
# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# WAP to print first 5 odd numbers:

# for i in range(3, 12):
#     print(i)

# a = 5

# for i in range(a):
#     print('Saturday Saturday') # how many times? 01234

# while a < 6:
#     print('Saturday Saturday') # infinite


# while a:
#     print(a.pop(0))

# x = "HELLLaHEaLLLO"
# for char in x:
#     if char.islower():
#         continue
#     print(char)
# print('Out of the loop')


# list = [3, 6, 9, 12, 16, 18, 21]
# WAP to check if all the numbers in the list are divisible by 3
numbers = [3, 6, 9, 12, 16, 18, 21]
# for number in numbers:
#     if number % 3 != 0:
#         print(f'{number} is not divisible by 3')
#         break
# else:
#     print("Execution of the loop completed without any break")
#     print("All the numbers are divisible by 3"

"""
WAP to reverse the elements in the list if the element is of the type string or else keep it as it is

"""
elements = ['Python', 'Java', 678, 9, 10, '876']

for elem in elements:
    # if type(elem) == str:
    #     print(elem[::-1])
    # else:
    #     print(elem)
    if isinstance(elem, int):
        print("integer", elem)
    else:
        print(elem[::-1])