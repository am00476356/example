"""
DRY -- Don't Repeat Yourself

Same piece of code shouldn't be written over and over again

functions
basically piece of code that written once can be called over and over again.

def func_name(arguments: optional):
    block of code[for repetition]

    // [optional] return ?

def : keyword
func_name : variable/identifiers
arguments : optional::we have to satisfy
block of code : what you want to do
return : after processing what you want to give back to the user.


# function and method::
function is independent
and method is basically a function inside a class


arguments:

default argument

* keyword arguments
* positional arguments


** lambda functions


modularity
code ko different parts chunks me partition karna


positional arguments

*args :: n number of positional arguments
*args --> n number of arguments in a tuple

packing and unpacking
all values into single tuple --> packing
single tuple values into individual values --> unpacking
[*] tuple


keyword arguments

**kwargs :: n number of keyword arguments.
[**] --> packing into dict
unpack using **


without def:
incognito -  anonymous

lambda functions
lambda input:output
lambda :: keyword
input can be n number
output can be only one [returned value]

"""

# WAP to add 34, 56 and 78, 889, and 24,43

# a = 34+56
# print(a)
# b = 78+889
# print(b)
# c = 24+43
# print(c)


# def add_two_numbers(a, b):
#     c = a+b
#     print(c)
#     return "Hello world"
#
#
# a = add_two_numbers(34, 56) #None
# print(a)
# b = add_two_numbers(78, 889)
# c = add_two_numbers(24, 43)
# d = add_two_numbers(a, b)
# e = add_two_numbers(d, c)


# WAF to greet some one

# def greet(name='Visionary'):
#     print(f"Hello {name} How are you doing?")
#
#
# greet()


name = "Visionary"

# def greet(name='Hello'):
#     print(name)
#     print(f"greeting for the day {name}")
#
# greet(name="Python")
# print(name)


greet = lambda x: f'greetings for the day {x}'
print(greet('Python'))

"""
lambda are heavily used in places where logical functioning
Reversed()

sorting -->
price high to low
price low to high
price between x to y
"""
