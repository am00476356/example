"""
inheritance?


Home - Parent
    Myself
"""

# B is the child of A --> B has its own properties+behaviour and its parents'
# property --< attributes
# behaviour --< methods

#
# class A:
#     tune = "Malhar"
#
#     def song(self):
#         print("Some song")
#
#
# class B(A):
#     director = "Gabbar"
#
#     def song2(self):
#         print("Khatarnaak Song")

# b = B()
# a = A()
# a.song()
# print(a.tune)
# b.song2()
# print(b.director)
# print(b.tune)
# b.song()

# child class has its own properties and behviour + the properties and behaviour of its parent.
# this acquiring of the prop/behaviour from its parent is called Inheritance.


# Single child - single Parent
# multiple child

class Parent:
    attrib1 = "Parampara"
    attrib2 = "Pratishta"

    def land(self):
        print("500 acres")

class Child1(Parent):
    pass

class Child2(Parent):
    attrib3 = "Khudgarz"

    def land(self):
        print("200 acres")

c1 = Child1()
c1.land()
c2 = Child2()
c2.land()
c2.land()
print(c2.attrib1)
print(c2.attrib2)
print(c2.attrib3)

# method over riding --> existing method, same name ko fir se define karna


class P1:
    attrib1 = "Hello"

    def greet(self):
        print("Hello ....")

class P2:
    attrib2 = "World"

    def greet(self):
        print("..................")

class C1(P1, P2):
    attrib = "Greed"


c1 = C1()
print(c1.attrib)
print(c1.attrib1)
print(c1.attrib2)
c1.greet()
# S == > ........ ? over ride

# MRO --> method resolution order
print(C1.__mro__)


class P1:
    attrib = "Hello"

class P2(P1):
    attrib = "hello"
    attrib2 = "World"

class C1(P2):
    pass

c1 = C1()
# print(C1.__mro__)
print(c1.attrib)

# parent has init and child has init.
