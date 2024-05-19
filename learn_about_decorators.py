"""
Decorators

Sajane -->
Fridge --> Main purpose serve is to cool
    [Cover]
    [Magnets]
    [Notes]
Wall -- main purpose
    painting -- deco

Door --
    painting


Writing functions that adds a functionality to original function.

caller function
    --> Decorator ==> caller function + decoration

* Decorators which arguments.
* Decoration can be done on top of decoration.
"""
def outer(func):
    def inner(*args, **kwargs):
        print("Additional functionality")
        return func(*args, **kwargs)
    return inner


def info(func):
    def wrapper(*args, **kwargs):
        print("INFO: THIS IS DECORATED ON TOP")
        return func(*args, **kwargs)
    return wrapper

@info  # outer = info(outer)
@outer # adder = outer(adder)  adder = info(outer(adder))
def adder(a, b):
    return a+b

@outer # sub=outer(sub)
def sub(a, b, c):
    print(a-b-c)

# print(adder)
# adder(1, 2)

# WAF to print a statement with a decorator saying what kind of statement it is.
# "Hello World"
# INFO: "Hello World"


# <function outer.<locals>.inner at 0x000001956800EB90>
# Additional functionality
# 3


# <function adder at 0x000001BCEB1DEB00>
# 3

# def delay(func):
#     """Delays the functionality by 5 secs"""
#     def wrapper(*args, **kwargs):
#         import time
#         time.sleep(5)  # Need to have this as dynamic value
#         return func(*args, **kwargs)
#     return wrapper


# def delay(func): # delay(greet)
#     """Delays the functionality by 5 secs""" # doc string
#     def wrapper(*args, **kwargs): # wrapper(any positional and any keyword args)
#         import time
#         time.sleep(5)  # Need to have this as dynamic value # line 74 nad 75 are addnl functionalities
#         return func(*args, **kwargs) # None
#     return wrapper #address of function at line number 73?? -->
#                      that is the function holding both additional and basic functionality


# @delay  # greet = delay(greet) # greet = wrapper(*args, **kwargs)
# def greet(name):
#     print(f'Hello {name}')


# greet("Dhoni")


# Now I need to get rid of constant 5 secs of delay but
# it should be parameterized in a fashion that when
# I pass any time the delay should be of that much time

# PARAMETERIZED DECORATOR

def delay(n):
    """Delays the functionality by n secs"""
    def outer(func):
        def wrapper(*args, **kwargs):
            import time
            time.sleep(n)  # Need to have this as dynamic value
            return func(*args, **kwargs)
        return wrapper
    return outer

@delay(1) # greet = delay(1) => outer(greet) => wrapper(name) => greet(name)
def greet(name):
    print(f"Hello {name}")

@delay(5)
def meet(name):
    print(f"Meeting with {name}")

# greet("World")
# meet("Foo")


# define a function that takes two numbers as input
# subtract it and return the positive difference.


# def sub(a, b):
#     return a-b


# Write a decorator to execute a function for three times

# def do_thrice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper

def re_doer(times):
    def re_doer_inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return re_doer_inner


@re_doer(2)
def sub(a, b):
    print(a-b)
    return a-b


@re_doer(5)
def greet(name):
    print(f"Hello {name}!")

sub(8, 2)
greet("Foo Bar")

# re_doer() parameterized function caller