"""
conditions???
condition as per programming is something that returns a boolean value.
if it doesn't return a boolean value, python as a language forces bool on it.

bool(1+5) ==> True/False

conditions are derived based on the requirements.
maybe there are different actions to be done based on the condition.


Conditional Statements

if

Syntax :
if condition:
    code/action

if True:
    then execute the code

if False:
    do not execute the code



if - else

Syntax:
if condition:
    [1]block of code
else:
    [2]block of code


if True:
    [1] is executed

if False:
    [1] is not executed
    [2] is executed


if - elif - else:
Syntax:
if condition:
    [1]block of code
elif condition2:
    [2]block of code
.
.
.
.
.
else:
    [3]block of code

if True:
    [1]

if False, elif True:
    [2]

if False, elif False:
    [3]

inline if-else:
True statement if condition else False Statement

nested-if
if condition:
    if condition:
        statement
    elif

    else
if block inside another if block.
"""

# WAP to check if the given element is present in the collection or not
# list, tuple, set, dict, string

breakfast = ['khakhra', 'jalebi', 'fafda', 'thepla', 'bread']
check_value = 'jalebi'

# if check_value in breakfast:
#     print(f'The {check_value} is present in the {breakfast}')


# WAP to check if the given element is present in the collection or not, if not add it the list
if check_value in breakfast:
    print(f'The {check_value} is present in the {breakfast}')
else:
    breakfast.append(check_value)
    print(f'{check_value} is added to the list')
    print(breakfast)

# WAP to check of the name starts with 's' or 'p' else declare not a student of current class.
# name = 'hello world'
# name = 'srk'
name = 'prk'
if name.startswith('s'):
    print('name started with s')
elif name.startswith('p'):
    print('name started with p')
else:
    print('not a student of the class')


# WAP to check if the number is greater 10 if yes return the number else return 10
# number = 9
# output_number = number if number > 10 else 10
# print(output_number)

# WAP to check if the string is palindrome or not using inline if else
