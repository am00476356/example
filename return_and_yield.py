"""
WAF which takes n as input and declares either a Wierd or Not Wierd
Given an integer,n , perform the following conditional actions:

    - If n is odd, print Weird
    - If n is even and in the inclusive range of  to , print Not Weird
    - If n is even and in the inclusive range of  to , print Weird
    - If n is even and greater than , print Not Weird
"""

"""
return - returns the value after 'return' keyword to the caller.
        first encounter of return and the callable gets terminated.
        
        Can I write multiple return statements?
            - Yes, but if in the same block then first return statement will be executed.
            - Conditionals should be present to manipulate what is to be returned
* caller?
* callable
* called

yield

"Lazy iterable"
if some callable is yielding data it is a generator.

_ : throw away variable

"""


# def check_if_input_is_odd(number):  # boolean True or False
#     if number % 2 == 0:
#         return False
#     else:
#         return True

# def convert_upper(name):
#     return name.upper()
#     return name.lower()
#     return name.title()


# z = check_if_input_is_odd(34) # False
# print(z)

# u = convert_upper("hello")  # HELLO
# print(u)


# def dad():
#     money = [100, 200, 500, 1000]
#     return money
#
# def mom():
#     money = [50, 100, 200, 500, 1000]
#     # money = "paisa paisa"
#     yield from money
#
# palak = dad()
# # print(palak)
#
# sanjit = mom()
# print(sanjit)
# print(next(sanjit))
# print(next(sanjit))
# print(next(sanjit))
# print(next(sanjit))
# print(next(sanjit))
#
# # items = ["a", "b", "c", "d"]
# #
# # for _ in items:
# #     print(i)
#
# for _ in range(5):
#     print("Hello")


def something_with_return():
    l = [1, 2, 3, 4, 5]
    for i in l:
        return i


def something_with_yield():
    l = [1, 2, 3, 4, 5]
    for i in l:
        yield i


_return = something_with_return()
print(_return)
#S = [12345]
#P = [12345]
#S1 = [12345]

# 1

_yield = something_with_yield()
print(_yield)
print(next(_yield))
print(next(_yield))
print(next(_yield))
print(next(_yield))
print(next(_yield))
print(next(_yield))
#S = 12345
#P = 1
#S1 = 1

# Nothing --> generator object