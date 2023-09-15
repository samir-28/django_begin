
#     color ='red'
#     def sound(self):
#         print('vroom vroom')
        
# fz=Bike()
# x=fz.color
# y=fz.sound()
# print(x)
# print(y)


class Bike:
    def __init__(self,color):   #constructor
        self.color=color
    def sound(self):
        print('...')
bike1=Bike('blue')
print(bike1.color)
print(bike1.sound)
