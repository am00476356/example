''' rivision of decorators'''

"""
Decorators: Add additional functionality on top of main functionality
"""


def outer(func):
    def inner(*args, **kwargs):
        print("Additonal Functionality")
        return func(*args, **kwargs)
    return inner


@outer  # adder = outer(adder) = inner
def adder(a, b):
    print(a+b)
    return a+b

# @outer # sub = outer(sub)
# def sub(a, b, c):
#     print(a-b)


output = adder(5, 6) # inner(5, 6)
print(output)

# sub(3, 2)