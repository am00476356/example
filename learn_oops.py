import random
"""
functional programming
    datastructures - list, string, int, dict and their operations
    conditional
    looping - for while, for else
    functions - re-usability and modularity
    example - C

Object Oriented Programming
    example - Java, Python, C++
    Python --> Purely Object Oriented Programming language even the builts have objects of various classes
    supports duck typing hence on the fly you can change the object.
    class
        - objects
        then we work on these objects.
    class?
        skeleton - structure
        :: Members
        :: Methods
        class me values/properties store -- class attributes
        class me functionalities -- methods

    create objects and use them.


    creating class

    class ClassName:
        attribute = value

        def method_name(self):
            pass

    class : keyword
    ClassName : Identifier [name of the class] - TitleCase - PEP8
    attribute : identifier name
    self : identifies that you are working with the object.
        - self can be anything, but standard is to write self
        - two objects self, other

    object creation:
        object_name = ClassName()

    dir --> displays all the attributes and methods of the class.

    Constructors:
        during object creation I take inputs for the user and give it to the object.
        1. take in values during object creation
        2. verification and obstruction.
"""


# class Human:
#     Age = 56
#     Gender = 'queer'  # one who is still searching who is s/he/it?
#
#     def walk(self):
#         print("Walking....")
#
#     def speak(self):
#         print("Thank you for coming to Python")
#
#     def listen(self):
#         print("Hmmmmmmmmmm")

# anuj = Human()
# # anuj as an object of human class and then I can modify Anuj as per his behaviour.
# # but the class remains unaffected.
# anuj.Age = 99
# print(anuj.Age)
# anuj.walk()
#
# palak = Human()
# print(palak.Age)
# shreya = Human
# human = Human()
# print(dir(human))


class Calculator:
    def __init__(self, a, b):
        if not isinstance(a, int):
            raise TypeError
        if not isinstance(b, int):
            raise TypeError
        self.a = a
        self.b = b

    def add(self):
        print(f"sum of {self.a} and {self.b} is {self.a+self.b}")

    def sub(self):
        print(f"sub of {self.a} and {self.b} is {self.a-self.b}")


# user1 = Calculator(10, 20)
# user1.add()
# user1.sub()
#
# user2 = Calculator([1, 2], 20)

user1 = Calculator(100, 200)
user1.add()
users2 = Calculator(34, 56)
users2.sub()
users2.a = 99
users2.sub()
user1.sub()
############################################

"""
object based behaviours

classes defined as skeletons

real world entity -- how it will act?? --> object

Gmail- Login
successful login [different objects of the same code/class]

class, objects
gmail each user object --> core code in terms of classes

"""
# WAP to define a class for students. 2 methods activities define.

class Student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num

    def physics(self, marks):
        self.marks = marks
        print(f"{self.name} scored {marks} in Physics")

    def physics_recheck(self):
        self.marks += 10
        print(f"{self.name} scored {self.marks} after rechecking")

    def admin(self, fees_status):
        if fees_status:
            print(f'{self.roll_num} has cleared all his fees')
        else:
            print(f'{self.roll_num} has not cleared all his fees')

s1 = Student("DK", 123)
s1.physics(65)
s1.physics_recheck()

s2 = Student("Rama", 909)
s2.admin(False)

# Write a class named Bank which takes in input as Name, Address and Aadhar Number
# methods -- > display account number
#     --> add balance
#      --> withdraw

class Bank:
    def __init__(self, name, address, aadhar_number):
        self.name = name
        self.address = address
        self.aadhar_number = aadhar_number
        self.balance = 0
        self.account_number = random.randint(1342567, 7654321)

    def display_account_number(self):

        print(f"Your account number is {self.account_number}")

    def add_balance(self, amount):
        self.balance += amount
        print(f"new balance {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"latest balance is {self.balance}")

