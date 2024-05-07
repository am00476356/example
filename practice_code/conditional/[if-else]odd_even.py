"""
WAP to check whether a number is odd or even.


odd? even?
number%2
% - modulo [remainder or shesh]

agar number%2 should be zero --> even
nahi to odd

if condition1:
    [1]code
else:
    [2]code

x = 5
x == 5
"""

number = 1

# if number != 0 and number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# if number and number % 2 == 0:  # bool(number)
#     print("EVEN")
# else:
#     print("ODD")

if number == 0:
    print("ZERO")
elif number == 1:
    print("Neither ODD nor Even")
elif number % 2 == 0:
    print("EVEN")
else:
    print("ODD")
