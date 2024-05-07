class Calculator:
    def add(self, a, b):
        print(f'sum of {a} and {b} is {a+b}')

    def sub(self, a, b):
        print(f'sub of {a} and {b} is {a-b}')


user1 = Calculator()
user1.add(10, 20)
user1.sub(10, 20)