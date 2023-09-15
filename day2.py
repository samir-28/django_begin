   # mutable-we can change the content // uses mostly
   # immutable-cant change content   // least use in real world projec#t
#help(str)
""" x="Cristano"
print(x.upper())
z="Ronaldo"
y=x.islower()
w=z.isupper()
print(y)
print(w)
v=x+z
print(v) """

# Datatypes: LIST :like array but can store diffrent type of values /mutable / []
# TUPPLE:    like LIST  but immutable // ()
# SET:        for mathmatical set operation   /mutable   // on;y unique value is stored
# DICTONARY:  key and value pair   // key value must be immutable
""" x="samir"
y="bazgin"
print(id(x))  #prints the memeory address
#print(dir(y))

A={"1","2","3","4"}  #sets
B={"4","5","6"}  #sets
#z=A.union(B)   use of SET
z=A.intersection(B)  #Use of set
print(z)   """ 


""" #X=["a","b","c"]
X=[1,2,3,4,5,6,7]
#Y=(a,b,c,d,e,f)
#help(X)
print(type(X))
 #X.extend([8,9,10])
X.append(8) # adds 8 in the list X
print(X)
print(len(X))  # prints the length of the list
print(X[2])
 """


""" # tupple
x=(1,2,3,3,4) # tupple
#x=(
print(type(x))  #prints the type of x :tupple
print(x)
print(len(x))
x=None  #mainly use to check noolean value
# x=(1,2,3,4,5,)
print(x)
 """
""" y=list({1,2,7,4,5,6}) # set of constructor // this line constrcuts list as list is indicated
print(y)

 """
 
""" # Dictonary
user={'name':'Cristano Ronaldo',
      'Gender':'Male',
      'Age':'38'}
print(type(user))
#print(user)
print(user['name'])  # prints name only
print(user.get('name'))  # prints name only
print(user.get('username','Default value'))# by using get we can be able to give dafault value if it is note available in list;
                                             #but if it is available it will print the value available in list 
user['Nation']='Nepal'  # update the key in dictonary
print(user) #prints upadated list including key :(Nation)
user.update(district='kavre') # update key in dictonary
print(user)  #prints upadated list including key :(distrcit)
print(user['district']) #prints the value available in district
print(user.get('district','default')) #this prints the value kavre as it is in list else it will print value that is mention i.e dafault in this line
print(user.keys())    # prints the keys of dictonary
print(user.values())   #prints the values of dictonary 
"""
 
# Conditional statements
""" marks=50
if marks < 40:
   print('fail')
elif marks < 60:
   print('okey')
else:
   print('Excellent')
 

marks=int(input("Enter the marks of student:"))
if marks >40:
   print(marks,'is fail')
else:
   print(marks,'is pass')
   """

#loopss

#For lop and while loop // do while is not used in python
 #x=[1,2,3,4,'samir']
#for item in x:   # for loop
 #  print(x)   jati ota index  xa teti choti x ko list print hunxa
 #print(item)  # jati ota item xa tei item matrai print hunxa
 
 
"""
 #task
x=[1,2,3,4,5,6,7,8]
for item in x:
   if (item % 2 ==0):
        print(item)
   else:
      print("odd number")
      print(item)
      """
#Assignment
# add insert,update,delete in datatypes of all
# use loop in all
# type casting ko concept
#python documentation  tutorial hell







 