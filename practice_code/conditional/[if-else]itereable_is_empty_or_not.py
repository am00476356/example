"""
WAP to check if the iterable is empty or not

itr = []
itr = ()
itr = {}
"""
itr = ()

if itr:
    print('Not Empty')
else:
    print('Empty')

# if not itr:
#     print('Empty')


# itr = []
# if itr == [] or itr==bool({}) or set() or ():
#     pass

# default value concept
# c1 : itr == [] # True
# c2 : {} ==> bool({}) # False
# c3 : set() ==> bool(set()) # False
# c4 : () ==> bool(()) # False
