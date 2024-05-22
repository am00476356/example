# def delay(func):
#     Delays the functionality by 5 secs
#
#     def wrapper(*args, **kwargs):
#         import time
#         time.sleep(5)  # Need to have this as dynamic value
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay
# def greet(name):
#     print(f'Hello {name}')
#
# greet("Dhoni")


# Now I need to get rid of constant 5 secs of delay but
# it should be parameterized in a fashion that when
# I pass any time the delay should be of that much time

def delay(seconds):
    def outer(func):
        def wrapper(*args, **kwargs):
            import time
            time.sleep(seconds)  # Need to have this as dynamic value
            return func(*args, **kwargs)
        return wrapper
    return outer


@delay(5)
def greet():
    print("Hello World")

greet()
