class Motorcycle:
    def __init__(self, top_speed, number_of_wheels):
        self.top_speed = top_speed
        self.number_of_wheels = number_of_wheels

    def drive(self):
        print(f"riding on my Motorcycle with {self.number_of_wheels} wheel")

    def mechanic(self):
        print("Not needed, new bike")


class Car:
    def __init__(self, top_speed, number_of_wheels):
        self.top_speed = top_speed
        self.number_of_wheels = number_of_wheels

    def drive(self):
        print(f"driving on my Car with {self.number_of_wheels} wheels")

    def mechanic(self):
        print("Not needed, new Car")


passion = Motorcycle(100, 2)
re = Motorcycle(160, 2)
audi = Car(360, 4)
ferrari = Car(560, 4)

list_vehicles = [passion, re, audi, ferrari]

for obj in list_vehicles:
    obj.drive()

# class Employee:
#
#     def salary(self):
#         print('salary')
#
# class CEO:
#
#     def salary(self):
#         print('draw salary')
#
#
# salary_slip_generation = ['all employee data'].salary()
