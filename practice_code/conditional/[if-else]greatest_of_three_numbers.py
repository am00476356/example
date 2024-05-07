"""
WAP to find greatest of three numbers
a, b, c = 14, 41, 11
"""
a, b, c = 17, 101, 11

# if a>b and a>c:
#     print(f'{a} is greatest')
# elif b>c:
#     print(f'{b} is greatest')
# else:
#     print(f'{c} is greatest')

maximum = a
if b > maximum and b > c:
    maximum = b
elif maximum < c:
    maximum = c

print(f'greatest is {maximum}')

