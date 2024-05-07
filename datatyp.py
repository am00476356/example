"""
Datatypes::

a = 10
123/-123
45.54
True/False
'String'
1+2j --> complex number


integer -- whole numbers
Float -- decimal numbers
Boolean -- True or False
str -- ordered collection of characters
complex numbers -- complex numbers

my_variable = int/float/decimal/boolean/complex/str

definition --> I dont have to tell what is the value or what type of value I want to assign


Type Conversion

Convert from 1 datatype to another

classname[in which I need to convert](I need to pass what needs to be converted)

❌ I can't convert complex to int
int can be converted to complex

int can be converted to string but all strings can't be converted to int.
And when conversion can't be done we get ValueError

Boolean can be converted:

Default values of the following results to boolean False, rest all the values results into Boolean True:

int = 0
str = ''
float = 0.0
complex = 0j or 0+0j
boolean  = False


### TASK 1 ###
chart stating what can be converted and what can't.

int --> str/float/complex/bool

Basic Operations

+  == addition
-  == sub
/  == div [Exact Float]
*  == multiplication
** == exponent (a to the power b --> a**b)
// == Floor division --> quotient
%  == Modulo --> remainder

mixed fraction -->22/3 ==> 7--1/3

### TASK 2 ###
1. WAP to find area of a rectangle.
2. WAP to find area of a triangle.




3. WAP to find to find the following output
team_a = "CSK"
team_b= "RCB"
team_a vs team_b # CSK vs RCB


45//3 = 15
45%3 = 0
44%3 = 2

45%11 = [0-10]

% --> output can range only 0-(n-1)
// --> can be anything 0-infinity


a = b+c
a = a+b

Marc has 5 tasks in hand
His manager gave him 3 more
how many task Marc has in hand now?

task_in_hand = 5
manager_tasks = 3
task_in_hand = task_in_hand + manager_task

a = 5
b = 3
a = a+b
a += b


Strings --> ordered collection of characters

browser = "CHROME"
browser2 = "EDGE"

# I can use single characters --> positions called index
# and python uses came characters across all the strings

"""
a = "Hello"

x = "####!!!!###hello######!!!!#"
# b = "hello world"
# print(a.capitalize())
# print(a.count('l'))
# print(a.endswith('d'))
# print(a.startswith('H'))
# print(x.strip())  # data cleaning
# print(x.strip('#!'))  # data cleaning
# print(x.lstrip('#!'))
# print(x.rstrip('#!'))

c = "CSK vs RCB"
# WAP to get the team names
# output = c.split('vs')
# print(output)

sentence = "Hello Palak are you still in call?"
# output = sentence.split()
# output = sentence.split(sep=' ', maxsplit=4)
# output = sentence.split(sep='are', maxsplit=4)
# print(output)

# print(sentence.index('l'))
print(a.rindex('l'))

# functions of string --> operations which you can perform over a string

# input data --< str
# PROCESS == functions == output
# output -->
##############################################################################
"""
int, float, complex, boolean

shopping_list = "jeans, shirt, t-shirt"
shopping_list = [jeans, shirt, t-shirt]

List??
list is a heterogeneous collection of datatype which can be changed

to define a list i need to enclose within []

- append --> adds element to the list at last (index increase) [rigid]
- pop --> removes element from last by default behaviour but 
            if I pass the index it removes the element at index
- clear --> removes everything and convert into empty list
- insert --> to add element at the given index
- copy
- count
- index



if I use append to add and pop to remove without any arguments--> LIFO Last in First Out

If I type cast string into list, it converts the string into list of characters
boolean of empty list is False rest is True
"""
list_a = ['jeans', 'shirt', 't-shirt']
list_b = [1, 'Hello', 4.5, True]
print(list_b)

# list_of_RR_matches_result = [True, True, True, True, False]
# list_of_RR_matches_result.append(False)
# print(list_of_RR_matches_result)
#
# list_of_students_attending_today = ['a', 'b', 'c']
# list_of_students_attending_today.pop()

list_a.pop()
