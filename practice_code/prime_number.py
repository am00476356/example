# Check if the number is prime or not

## generate numbers between 2, n-1
## Loop Control Statements -- pass, break, continue
## For, while, For-else

n = 872295555153497
# n = 25
# output = list(range(2, n))
# print(output)
# prime_flag = False
# for i in range(2, n):
#     if n % i == 0:
#         prime_flag = False
#         break
#     else:
#         prime_flag = True
#
# if prime_flag:
#     print("The number is Prime")
# else:
#     print("The number is Non-prime")

# for i in range(2, n):
#     if n % i == 0:
#         break
# else:
#     # when without break loop
#     print("Prime Number")
#
#
# for i in range(2, (n//2)+1):
#     if n % i == 0:
#         break
# else:
#     # when without break loop
#     print("Prime Number")

import math
for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0:
        break
else:
    # when without break loop
    print("Prime Number")

"""
Not Prime
Not Prime
Prime
Prime

n=6
1. loop --> 2, 3, 4, 5
    i = 2.
    if 6%2 == 0 --> 0
    i = 3
    if 6 %3 == 0 --> 0
    i = 4
    if 6%4 == 0 --> 2
    i = 5
    if 6%5 == 0 --> 1


n=25
Prime
Prime
Prime
Not prime
loop --> 2, 3, 4, 5, 6, .. 24
    1
    
25 --> 13
25 --> 3
"""