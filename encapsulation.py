"""
encapsulation
wrap the data and methods into a single unit
capsule :: mix of things presented in a single entity
 - pp 1 gm
 - zz 2gm
 - ww 1gm
 - ee 0.5gm
"""
# class A:
#     a = 5
#
#     def hello(self):
#         pass


# password should be min 8 characters
# class SignUp:
#
#     def __init__(self, username, pwd):
#         self.username = username
#         self.pwd = pwd
#         if len(self.pwd) < 8:
#             raise ValueError("Please enter a min of 8 characters")
#
#     def sign_up(self):
#         print("Signup successful")
#
#     def print_pwd(self):
#         print(self.pwd)
#
#     def print_username(self):
#         print(self.username)


# user1 = SignUp("aka", "123468329")
# user1.sign_up()
# user1.pwd = "123"
# user1.print_username()
# user1.print_pwd()
# del user1.username
# # print(dir(user1))
# user1.print_username()

"""
Issue 1 : They can't change the behaviour once added.
Issue 2 : When changing the behaviour the same restrictions should be applied.
When done via init --> object creation is protected but later can be modified.

Issue 3 : deletion of attributes should be controlled.


Getter-Setter-Deleter
"""
class SignUp:

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

    @property
    def pwd(self):
        return self.pwd()

    @pwd.setter
    def pwd(self, value):
        if len(value) < 8:
            raise ValueError("Pwd should be min 8 characters")
        self._pwd = value

    @pwd.getter
    def pwd(self):
        return self._pwd

    @pwd.deleter
    def pwd(self):
        raise AttributeError("can't delete pwd")

    def sign_up(self):
        print("Signup successful")

    def print_pwd(self):
        print(f"{'*'*len(self.pwd)}")

    def print_username(self):
        print(self.username)

# # user1 = SignUp("aka", "123") # object creation is handled [with wrong data]✔️
# user1 = SignUp("aka", "123456789") # object creation is handled [with right data]✔
# # user1.pwd = "123" # updation after object creation is also verified ✔️
# user1.print_pwd()
# del user1.pwd


"""
Public member, private members and protected members
var_name :: Public members, called and used by end user.

_var_name :: Internal Use only. Touch only when you are an expert.

__var_name :: Protected.


Logic _logic1[] _logic2[] _logic3[]
_logic1()
_logic2()
_logic3()
"""

class A:
    foo = "FOO"
    _hello = "Hello"
    __world = "WORLD"

a =A()
print(a.foo)
print(a._hello)
# print(a.__world)
print(dir(a))
