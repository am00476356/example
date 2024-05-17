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

def delay(func):
    """Delays the functionality by 5 secs"""
    def wrapper(*args, **kwargs):
        import time
        time.sleep(5)  # Need to have this as dynamic value
        return func(*args, **kwargs)
    return wrapper


# def delay(func): # delay(greet)
#     """Delays the functionality by 5 secs""" # doc string
#     def wrapper(*args, **kwargs): # wrapper(any positional and any keyword args)
#         import time
#         time.sleep(5)  # Need to have this as dynamic value # line 74 nad 75 are addnl functionalities
#         return func(*args, **kwargs) # None
#     return wrapper #address of function at line number 73?? -->
#                      that is the function holding both additional and basic functionality


@delay  # greet = delay(greet) # greet = wrapper(*args, **kwargs)
def greet(name):
    print(f'Hello {name}')


greet("Dhoni")


# Now I need to get rid of constant 5 secs of delay but
# it should be parameterized in a fashion that when
# I pass any time the delay should be of that much time