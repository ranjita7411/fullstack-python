# class bank:
#     def __init__(self):
#         self.__balance=10000
#     def deposite(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         print(self.__balance) 
# account=bank()
# account.deposite(5000) 
# account.show_balance()      


###getter
# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
# emp=employee(736383)
# print(emp.get_salary())    

###setter
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def set_salary(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

# emp = Employee(50000)
# emp.set_salary(60000)
# print(emp.get_salary())

# class employee:
#     def __init__(self):
#         self.__salary=0
#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary=amount
#         else:
#             print("invalid salary")

#     def get_salary(self):
#             return self.__salary
# emp=employee()
# emp.set_salary(7364876)
# print(emp.get_salary())    

##polymorphism
# class dog:
#     def sound(self):
#         print("dog barks")
# class cat:
#     def sound(self):
#         print("cat meaw")

# Dog=dog()
# Cat=cat()
# Dog.sound()
# Cat.sound()

# class car:
#     def move(self):
#         print("Car is driving")

# class bike:
#     def move(self):
#         print("Bike is riding")

# Car = car()
# Bike = bike()
# Car.move()
# Bike.move()

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")

car=car()
car.start()