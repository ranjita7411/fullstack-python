# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("ram",21)
# s2=student("sita",20)
# s3=student("ravan",23)
# print("name:",s1.name)
# print("age:",s1.age) 
# print("name:",s2.name)
# print("age:",s2.age)        
# print("name:",s3.name)
# print("age:",s3.age)               

# class student:  # class   name
#     name = "venny"  # attribute
#     def study(self):   #represent current object
#         print("venny is sleeping")
# s1 = student()         #s1 is a object
# print(s1.name)
# s1.study() # study is a method

# class student:
#     def details(self):
#         print("had breakfast")
# s1 = student()
# s1.details()

# student.details(s1)

# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def check_balance(self):
#         print(self.balance)
# account=bank(5000)
# account.check_balance()    

# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"logged in")
# u1=user("nibba")
# u1.login()
# u2=user("nibbi")
# u2.login()            
           

##inheritance#### 

# class father():
#     def house(self):
#         print("father has a house")
# class son(father):
#     def bike(self):
#         print("son has a bike")
      
# s=son()
# s.house()
# s.bike()
                        
# class grandfather:
#     def lanf(self):
#         print("grandfather's land")

# class father(grandfather):
#     def house(self):
#         print("father's land")

# class son(father):
#     def bike(self):
#         print("son has a bike")

# obj = son()

# obj.house()
# obj.bike()

##multiple heritance
# class appa:
#     def house(self):
#         print("appa's house")
# class amma:
#     def car(self):
#         print("amma's car")
# class maga(appa,amma):
#     def bike(self):
#         print("maga's bike")
# thirdclass=maga()
# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()                        
              
# class Father:
#     def land(self):
#         print("Father's land")

# class Son(Father):
#     def land(self):
#         print("Son's land")

# class Daughter(Father):
#     def land(self):
#         print("Daughter's land")


# father = Father()
# son = Son()
# daughter = Daughter()

# father.land()
# son.land()
# daughter.land()

###magic methods
###str()#####
##used for readable object output

# class student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
# s=student("king")
# print(s)        

# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("Hello python")
#     print("hey gopalan")
#     print("hi guys")
# hello() 
       
# import json
# student={
#     "name":"ram",
#     "age":22
# }
# data=json.dumps(student)
# print(data)

# import json

# student = {
#     "name": "ram",
#     "age": 22
# }

# json_data = json.dumps(student)
# print("JSON:", json_data)

# python_data = json.loads(json_data)
# print("Python:", python_data)
# print(type(python_data))


# import requests
# response=requests.get(
#     "https://api.github.com/users/python"
# )
# data=response.json()
# print(data)

