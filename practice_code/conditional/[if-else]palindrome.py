"""
WAP to check if the given string is palindrome or not?

ex - racecar
mom, NaN, SOS
"""

name = "racecar"
reversed_name = name[::-1]

# if name == reversed_name:
#     print("It is a palindrome")
# else:
#     print('Not a palindrome')

"""
WAP to check if the integer is palindrome or not.
"""
give_me_an_int = 565
a = str(give_me_an_int)
b = a[::-1]

if a == b:  # a is b will not work since the memory locations are different
    print("It is a palindrome")
else:
    print('Not a palindrome')

