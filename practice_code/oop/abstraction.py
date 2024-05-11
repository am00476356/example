from abc import ABC, abstractmethod


class Template(ABC):

    @abstractmethod
    def implement_me(self):
        pass

    @abstractmethod
    def hello(self):
        pass

    def world(self):
        pass

# t = Template()

class Implementation(Template):

    def implement_me(self):
        print("Implemented")

    def hello(self):
        print("Hello")


i = Implementation()



"""
Required fields are email and password.
Once the required fields are satisfied then you activate the LOGIN.

activate LOGIN == creating the object

* Coder 1

class Login:
    def init(email, password):
        .
        .
    
    def email()
        ..
        
    def pwd()
        ..
        
** Coder 2

class Login:
    def init(ema.., pwd)
        ..
        
    def email()
        ..
        
    def pwd()
        ..
        
Company --> Flexibility ❌
Create Templates and ask developer to implement it


"""

class LoginTemplate(ABC):

    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def password(self):
        pass


class BakeryLogin(LoginTemplate):

    def __init__(self, _email, pwd):
        self._email = _email
        self.pwd = pwd

    def email(self):
        print(f"email is entered {self._email}")

    def password(self):
        print(f"valid password is entered {'*'*len(self.pwd)}")

    def login_enter(self):
        print("Entering to Home Page")


user1 = BakeryLogin("john_doe@email.com", "foobar123")
user1.email()
user1.password()
user1.login_enter()
