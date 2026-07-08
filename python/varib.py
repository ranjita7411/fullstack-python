# product_price=5000
# delivery_charges=100

# total=product_price+delivery_charges
# print(total)

# a=10
# b=3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# student=10
# groups=2
# print(student//groups)

# followers=100
# followers=followers-1
# print(followers)

# saved_password="1234"
# entered_password="1234"
# print(saved_password==entered_password)

# balance=500
# pin_correct=True
# if balance>=1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")

# product=input("enter the product name:")
# price=int(input("enter the price:"))
# quantity=int(input("enter the quantity:"))
# discount=int(input("enter the discount percentage:"))
# total=price*quantity 
# final_bill=total-discount
# print("product:",product)
# print("total:",total)
# print("final bill:",final_bill)       

# age=20
# if age>=18:
#     print("eligible to vote")

#     marks=int(input("enter the marks:"))
#     if marks>=90:
#         print("cgpa=9")
#     elif marks>=75:
#             print("cgpa=7.5")
#     elif marks>=50:
#             print("cgpa")
#     else:
#              print("fail")


# age=25
# salary=50000
# if age>=18 and salary>=30000:
#     print("eligible for loan")

# day="sunday"
# if day=="saturday" or day=="sunday":
#     print("holiday")
# else:
#     print("working day") 

# pin=12345
# enter_pin=int(input("enter the pin: "))
# if enter_pin==12345:
#     print("login successful")
# else:
#     print("login failed")

# def withdraw_money():
#      pin=input("enter the pin: ")
# if pin=="1234":
#     amount=int(input("enter the amount: "))
#     balance=50000
#     if amount<=balance:
#         balance=balance-amount
#         print("withdraw successful")
#         print("remaining balance:",balance)
#     else:
#         print("insufficient balance")
# else:
#     print("invalid pin")
# withdraw_money()

# for i in range(5):
#      print("hello world!")
# users=["ram","shyam","hari"]
# for user in users:
#      print("message sent to",user)
# for i in range(1,6):
#      print(i)
# name="virat"
# for ch in name:
#      print(ch)

# count=1
# while count<=5:     
#     print(count)
#     count+=1

# for i in range(10):
#     if i==5:
#         break
#     print(i)    
# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# password=""
# while password!="1234":
#     password=input("enter password:")
#     print("invalid password")
# else:
#     print("login successful")   

student=[
    "ram",
    "shyam",
    "hari"
]
student.append("gita")
student.remove("hari")

print(student)