#function
# def func():  # def is for creating function
#     print("Hello")
    
# func()  #function call
 
 #  types: built and user defined function  
 
 
 
# def add(a,b):
#     return a+b

# # result=add(3,4)
# # print(result)


# def check_even(x,y):
#     sum=add(x,y)  // calls add function
#     result=False
#     if sum % 2==0:
#         result=True
#     return result
# res=check_even(4,7) //pass i place of a,b
# print(res)


# def func():
#     value=4
#     print('INside value',value)  // print value inside func

    
# value=8
# func()
# print(value)  //print value of outside func



# def my_func():
#     global v
#     v=5
#     print('Inside func',v)
# v=8  #prints 5 as it is global and inside function so...
# my_func()
# k=6  # prints 6     
# print(v)


# positional and keyword

""" def add(a,b):
    print('result:',a-b)
    
add(8,6)  # here a=8,b=6
    # positonal argument function ma jun order m aparameter pathako xa tei order ma value pathaune like a=5 and b=6
    
add(b=9,a=8) #this is keyword argument i,e we can assign value if we know know the function arguments name i.e a,b """

#lambda function(anyonomous function)


# add=lambda a,b:a+b   #argument and operation at same line
# x=add(1,2)
# print(x)


# square=lambda a:a*a
# c=int(input("Enter the number :"))
# z=square(c)
# print(z)

# # *args ,**kwargs 
# encapulation,class method ,static method
 



# class Bike:
#     color ='red'
#     def sound(self):
#         print('vroom vroom')
        
# fz=Bike()
# x=fz.color
# y=fz.sound()
# print(x)
# print(y)


""" class Bike:
    def __init__(self,color):   #constructor
        self.color=color
    def sound(self):
        print('...')
bike1=Bike('blue')
bike2=Bike('Green')
print(bike1.color)
print(bike2.color)
 """
 
""" class Vehicle:
    def __init__(self,color,doors):
        self.color=color
        self.door=doors
        
class Bike(Vehicle):  # inherit the parent :vehicle
    def get_doors(self):
        return self.get_doors
bike1=Bike('RED',1)
bike2=Bike('Blue',2)
print(bike1.color,bike1.door)    
print(bike2.color,bike2.door) """



""" #Django
M-Database   /(rdbms / ORM)
V-views /requestland/logic
T-template/basically HTML """



 