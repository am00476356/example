# to understand what happens when parent and child has init.

"""
* It is child's responsibility to take care of parents.
* It is child which has to satisfy all the init of all the parents which are present
* how do we satisfy?
    - call the init of parent.
    anything from parent if you want to call you use the keyword super()4


# can you have multiple inits in your class?
Yes! but only the last/latest init would work.

overloading
same naam se se multiple methods in the scope.

overriding
same method ko fir se re-write
"""


# bakery app where order, we stamp our names and process the order
class Bakery:
    def __init__(self, name_of_bakery):
        self.name_of_bakery = name_of_bakery

    def stamp(self):
        print(f"{self.name_of_bakery} stamped on the cover")


class Menu(Bakery):

    def __init__(self, product, name_of_bakery):
        self.product = product
        super().__init__(name_of_bakery)

    # def stamp(self):
    #     # over-riding stamp
    #     pass

    # def stamp(self):
    #     pass
    #
    # def stamp(self):
    #     pass
    def stamp(self):
        # over-ridden the parent stamp
        super().stamp()  # calling the parent stamp
        print("Seal the packaging")  # additional functionality

    def process_order(self):
        self.stamp()
        print(f"{self.product} is dispatched")


order1 = Menu("cake", "Mad Bakers")
order1.process_order()

class A:
# constructor overloading
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self, a):
        self.a = a


# a = A()
# P  - 1
# S1 - 3
# S2 - 3

class P:
    def __init__(self, p):
        self.p = p

class C(P):
    def __init__(self, p):
        super().__init__(p)

    def child(self):
        pass

c= C(1)
