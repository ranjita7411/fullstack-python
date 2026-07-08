# student=("ram","shyam","hari")
# print(student[-2])
# numbers=(10,20,30)
# print(numbers[-3])

# data=(1,2,3)
# data[0]=1
# print(data)

# x=(1,2,3,2,1,1,1)
# print(x.count(1))
# print(x.count(2))

# y=("souj","souj","ram","ram","sita","sita","sita","souj")
# print(y.index("souj"))
# print(y.index("ram"))

# y=("souj","souj","ram","ram","sita","sita","sita","souj")
# print(y.count("souj"))
# print(y.count("ram"))
# num=(10,20,30,40,50)
# print(num[1:4])

# num=(10,20,30,40,50)
# print(num[::-1])

####sets###
#set is collection of remove duplicate valuue and store unique value:no indexing:unordered
#list:square bracket tuples:parenthesis  sets:flower bracket

# x={2,3,4,1,1,1,1,2,2,5,6,5,4}
# print(x)

# data={1,2,3}
# data.add(4)
# data.remove(2)
# print(data)

# a={1,2,3}
# b={3,4,5}
# print(a|b)

# a={1,2,3}
# b={3,4,5}
# print(a&b)

######function#####

# def greeting():
#     print("Hello World!")
# greeting()

# def add():
#     return 10+20
# result=add()
# print(result)

# def add(a,b):
#     print(a+b)
# add(10,20)    

# def sub(a,b):
#     print(a-b)
# sub(30,20)    

# def divide(a,b):
#     print(a/b)
# divide(30,2) 

# def multiply(a,b):
#     print(a*b)
# multiply(3,2) 

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40)    

# def dinga(*numbers):
#     print(numbers)
# dinga(10,20,30,40)    

# def ram(*num):
#     total=0
#     for i in num:
#         total+=i
#     print(total)
# ram(10,20,50)    

######**kwargs######
# def students(**details):
#     print(details)

# students(
#     name="ram",
#     age=22,
#     job="sales",
# )   

# def student(**details):
#     print("name:",details["name"])
#     print("age:",details["age"])
#     print("job:",details["job"])
# student(
#     name="ram",
#     age=22,
#     job="sales",
#     )    
# def sqrt(num):
#     return num*num
# print(sqrt(5))
    
# def sqrt(num):
#     return num**0.5
# print(sqrt(25))    

# sqrt=lambda x:x**0.5
# print(sqrt(25))

# square=lambda x:x*x
# print(square(5))

# add=lambda a,b:a+b 
# print(add(10,20))

# def odd_even(num):
#     if num % 2 == 1:
#         print(num, "is odd")
#     else:
#         print(num, "is even")

# number = int(input("Enter a number: "))
# odd_even(number)

# thima=lambda x:"even" if x%2==0 else "odd"
# print(thima(10))
# print(thima(7))

# num=lambda name:name .upper()
# print(num("ram"))

# num=lambda name:name .lower()
# print(num("RAM"))

# num=lambda text:len(text)
# print(num("ram"))

#


# file = open("student.txt", "w")
# file.write("hello world")
# file.close()
# print("Data written successfully")

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("student.txt", "a")   # Open file in append mode
# file.write("\nhey bruh")          # \n writes on a new line
# file.close()
 
 
 

# file = open("student.txt", "w")
# file.write("hello world")
# file.close()

# print("Data written successfully")

# file = open("student.txt", "r")
# data=file.read()
# print(data)
# file.close()

# file = open("student.txt", "a")
# file.write("\nhey bruh\n")
# file.close()

# print("data append successfully")

# file = open("student.txt", "r")
# print(file.read())
# file.close()


# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("something went wrong")    


# 2



# try:
#     a=int(input("enter A:"))  
#     b=int(input("enter B:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter only numbers")           

# try:
#     file=open("data.text")
#     print(file.read())
# except:
#     print("file error")
# finally:
#     print("program completed")


try:
    print(10/2)
except:
    print("error")
else:
    print("success")        