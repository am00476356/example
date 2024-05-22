"""
Staticmethod, classmethod, property

# inbuilt decorators
1. staticmethod

- What is method?
    functions inside class
    - first argument is self --> object denote.
    - If my method doesn't use self anywhere inside its implementation, chances are there that the method is static.

    --> if it marked/decorated as @staticmethod, it is meant to not have self.
    ==> implies that object dependency is not there.

    So it is part of class but not dependent on object.

    to call static methods either:
        - call using object
        - call using class name
        -------- it will be called using ClassName.methodName

    StaticMethods are defined in cases where it is logical to keep the code together in the class
    but the method is independent of object.

2. classmethod
    Methods that take first argument as 'cls'--> class reference
    They are deorated with @classmethod.
    One of the Use case is :
        multiple decorators :: `OrderAtHotel`

3. property
makes a method to 'act' like an attribute
Useful in chaining mostly.
"""

# class MathematicalModel:
#
#     a = "Anonymous"
#
#     @staticmethod
#     def pythagorus_theorem(self):
#         """logic related to pythagorus theorem"""
#         pass
#
#     @staticmethod
#     def greeting(b):
#         print(f"hello {b}")

# Hello.greet()
# Hello().greet()


# class English:
#
#     @classmethod
#     def walk_english(cls):
#         cls.WALK = "WALKING ENGLISH"
#         print(cls.WALK)
#
# e = English()
# # English.walk_english()
# # print(e.WALK)
# print(dir(object))

class Browsers:

    chrome = "GOOGLE"
    firefox = "MOZILLA"

    @property
    def open_chrome(self):
        print(f"open chrome")

    def open_firefox(self):
        print(f"open firefox made by {self.firefox}")


# browser = Browsers()
# browser.open_chrome # open chrome
# # print(browser.firefox)