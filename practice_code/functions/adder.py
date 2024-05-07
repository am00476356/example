# def add_me(a=0, b=0, c=0, d=0):
#     return a+b+c+d
#
#
# x = add_me(1, 2, 3)
# print(x)
# y = add_me(1, 2)
# print(y)
# z = add_me(1, 2, 3, 4)
# pl = add_me(1)
# # dynamic
# # !flexible
# #

# google--> how to write a function to add infinite numbers

# def add_me(*args):
#     print(*args, sep="----")
#     # print(1, 2, 3, sep="----")
#     # a, b, c = args
#     # print(f'a = {a}')
#     # print(f'b = {b}')
#     # print(f'c = {c}')
#     return sum(args)
#
#
# x = add_me(1, 2, 3)
# print(x)
# # y = add_me(1, 2)
# # print(y)
# # z = add_me(1, 2, 3, 4, 6, 7, 8, 10, 11)
# # print(z)
# # pl = add_me()
# # print(pl)
#
#
# def add_using_keyword(**kwargs):
#     print(kwargs)
#     return sum(kwargs.values())
#
# f = add_using_keyword(b=7, a=5)
# print(f)

def adder(*args, **kwargs):
    return sum(args)+sum(kwargs.values())


# a = adder(x=5,y=50)
# print(a)

add = lambda x, y: x+y
print(add(5, 6))