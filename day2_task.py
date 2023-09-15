"""
# inserting data in list

x=[1,2,3,4,5,6]
x.extend([7,8])  #update 7,8 in list
print(x)

#deleting item
x.__delitem__(5)  #delete index no 5 item i.e 6
print(x)


# tupple
#inserting is not possible in tuple as it is not immutable but can be replace 
y=(1,2,3,4,5)
y=None
y=(1,2,3,4,5,6,7,8)
print(y)
 
 
 #set
 #inserting item
z={"cr7","kholi","dhoni","messi","mbappe"}
z.update(['samir'])
print(z)
#deleting item
z.remove('messi')
print(z)
    """
    
""" #Dictonary
w={'name':'samir','age':'19','height':'5.7','nationality':'nepali'}
print(w)
# print(w.keys())
# print(w.values())
# w['Gender']='male'  #update key and value
w.update(District='kavre')
# print(w.get('age')) #print age only
# print(w['name'])    #prints name only
print(w)

#delete
w.__delitem__('name')
w.__delitem__('nationality')
print(w)
 """
 
 
 
# #loops......
# x=[1,2,3,4,5,6]
# for item in x:
#     print(item)
    
    
    
# #task
# x=[1,2,3,4,5,6,7,8]
# for item in x:
#    if (item % 2 ==0):
#        print(item,"is even number")
#    else:
#        print(item,"is even number")
 
