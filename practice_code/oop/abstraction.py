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