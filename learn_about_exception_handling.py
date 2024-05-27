"""
Exception handling/ Error Handling
These can be faults at the logical part of the code or by the user inputs.


REST :: Representational State transfer
get
put
post
del

http :: hyper text transfer protocol

protocol:
    set of rules


404 :: page not found


"""


def divide(z, y):
    return z/y


#
# try:
#     x = divide(1, 4)
#     print(x)
# except:
#     print("Error is raised, Please re-evaluate")


# try:
#     x = divide(1, 4)
#     print(x)
# except (ZeroDivisionError, TypeError):
#     print("Error is raised, Please re-evaluate")

#
# try:
#     x = divide(1, 4)
#     print(x)
# except TypeError:
#     x = divide(int(1), int('1'))
#     print(x)
# except ZeroDivisionError:
#     print("Divisor can't be Zero, Please re-evaluate")


# try:
#     x = divide(1, 0)
#     print(x)
# except:
#     print("Error is raised, Please re-evaluate")
# finally:
#     print("Execution is completed....")

try:
    x = divide(1, 0)
except:
    print("Error is raised, Please re-evaluate")
else:
    print("Else is being executed")
finally:
    print("SRK")


"""
try:
    visit website goibibo.com
except "ibibo.com":
    redirect to goibibo.com

finally:
    return tab on chrome


try:
    launching the ad

finally:
    load the page
"""

class MyCustomException(Exception):
    pass
