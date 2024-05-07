"""
WAP to check whether a given character is lower or not

if condition:
    statement
else:
    statement else

condition
islower() --> True or False
"""
character = 'a'

# if character.islower():
#     print('Character is lower')
# else:
#     print('Character is not lower')

# you can't use any built-in functions
# ask? ('a', 'b', 'c' ... 'z')
# if  character in list:

# can I use ASCII/UNICODE?

value_in_int = ord(character)

# if value_in_int >= 97 and value_in_int <= 122:
# if value_in_int > 96 and value_in_int < 123:
if 123 > value_in_int > 96:
    print('Character is lower')
else:
    print('Character is not lower')
