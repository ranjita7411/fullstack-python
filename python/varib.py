product_price=5000
delivery_charges=100

total=product_price+delivery_charges
print(total)

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
student=10
groups=2
print(student//groups)

followers=100
followers=followers-1
print(followers)

saved_password="1234"
entered_password="1234"
print(saved_password==entered_password)

balance=500
pin_correct=True
if balance>=1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")

product=input("enter the product name:")
price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
discount=int(input("enter the discount percentage:"))
total=price*quantity 
final_bill=total-discount
print("product:",product)
print("total:",total)
print("final bill:",final_bill)       
