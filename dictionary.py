#Dictionary
"""Dictionary in Python is a collection of keys values , used to store data values like a map,which,unlike other data types which hold 
only a single value as an element.

In some langugages it is known as map or assosiative arrays

dict={'name:"nitish",'age':'33','gender':'male'}

Characterstics.
.Mutable
.Indexing has no meaning
.Keys cant be duplicated
.Keys cant be mutable items"""

#empty dic
# d={}
# print(d)
# #1d dic
# d1={'name':"nitish",'gender':'male'}
# print(d1)

# #with mixed keys
# d2={(1,2,3):1,'hello':'world'}
# print(d2)

#2D dict
s={
    'name':'nitish',
    'college':'bit',
    'sem':4,
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}
print(s)

#usingg type conversion
s4=dict([(1,1),(2,2),(3,3)])
print(s4)

s4=dict([(1,1),('age',2),(3,3)])
print(s4)

#Duplicate key--last onee print
s1={'name':'yash','name':'rahul'}
print(s1)

#mutable items as key
s5={'name':'nitish',(1,2,3):2}
print(s5)

#Accesing items(indexing not allowed)
my_dict={'name':'Yash','age':25}
#[]
print(my_dict['name'])
#get
print(my_dict.get('name'))

print(s['subjects']['maths'])

#Adding key_value pair
my_dict['gender']='male'
print(my_dict)

s['subjects']['datascience']=75
print(s)
#Remove key-value-pair
#pop
# d={'name': 'Yash', 'age': 25, 'gender': 'male'}
# print(d.pop(0))
d={'name':'nitish','age':32,3:3,'gender':'male','weight':72}
# d.pop(3)
# print(d)
# print(d)
#popitem--->remove last item
# d.popitem()
# d.popitem()
print(d)
#del
del d['name']
print(d)
#clear
d.clear()
print(d)

#Editing key-value-pair
print(s)
s['sem']=5
s['subjects']['datascience']=17
print(s)

#Dictionary Operations
#Membership-->specify key
print('yash'in s)#-->false(value)
print('name'in s)#True-->key

#iteration
d={'name':'yash','gender':'male','age':33}
for i in d:
    print(i,d[i])

#Dictonary Functions
#len/sorted
print(len(d))
print(sorted(d))
print(min(d))

#items/key/values
#items--convert value into tuple
print(d.items())
#key--all keys
print(d.keys())
#values
print(d.values())

#update
d1={1:2,3:4,4:5}
d2={4:7,6:8}
d1.update(d2)
print(d1)

#DICTIONARY COMPREHENSION
#{KEY:VALUE FOR VARS IN ITERABLE}

#print 1st 10 numbers and their squares
print({i:i**2 for i in range(1,11)})

#using existing dict
distances={'delhi':1000,'mumbai':2000,'banglore':3000}
print({key:value*0.62 for (key,value)in distances.items()})

#using zip
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
temp_c=[30.5,32.6,31.8,33.4,29.8,30.2,29.9]
{i:j for i,j in zip(days,temp_c)}

#Using if condition
products={'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:value for (key,value) in products.items()if value>0})

#Nested Comphrension
#print table of number 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})