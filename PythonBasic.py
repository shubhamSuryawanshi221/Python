
=====what is python=====
1.High level programming language:it is used various sectors
-web development
-software development
-machine learning
-AI
-Robotics
-Data science
-Data analytics
n number of sectors

2.interpreted programming language:
translator -converts python code ->machine code line by line in running time

debugging is very easy -handles the errors

3.Interactive programming language:
translator -converts python code ->machine code line by line before running program

communication between the developer and compiler

4.General purpose programming language:
by using python we can develop web apps/web sites/software
-web apps
-Android apps
-desktop apps
-IOS
-Games
-GUI
etc...

====advantages====
1.very easy
2.syntax is very less
3.cross platform -it supports multiple os
4.portable language -if we write code in windows same code we can run in Linux also
5.very short time we can develop complex apps
6.100+libraries
7.increse the productivity

====disadvantages===
1.slow speed      :code executed line by line
2.run time errors :identify errors

libraries and frame works both are predefined functions

in python we are using Django,tkiter frame works ->web apps/web sites

by usig pyton we can create thousands of applications
-intagam
-spotify
-google -web search system purpose
-youtube -video sharing purpose
-intel -testing prpose

python.org

=====python setup====
python has been installed or not we need to check with command prompt

command prompt ->python

IDLE -integrated development and learnig environment
code editor

#create new file

file_name.py
data.py
Bhaskar.py
chinni.py



====comment lines====
-it is used to make non executable code/never execute
-it is used to make some description about task

2types
#1.single line comment -#
#2.multi line comment  -''' ''' or """ """

====print statement===
-it is used print any kind of data
-it is a predefined function

print() -already defined

print(100)
100
print(3.4)
3.4
print(2+5)
7

===Data types===
#1.primitive data types
In single container we can store only one value

#3 types
#1.number:
   int -1,3,2,4,5,6,7,8 ->Normal numbers
   float-4.5,2.7,8.5,4.5 ->decimal numbers
#2.string:
-it is a group of alpha numeric characters
-string should be declare -"" or ''
-'123',133 we can not able to do mathematical calculations

#3.Boolean:
-True -1,false-0
-Boolean should be declare without -'' or ""
-True or False

print(100)
print(2.4)
print('python')
print(True)

====how to find which data type===
type() -predefined function

print(type(100))
print(type(20.6))
print(type('bhaskar'))
print(type(True))


====variable===
-it is a container blocks/groups
-it is used to store the data
-variable must be start with a-z or _
 ex:abc or Bhaskar or _abc 
-variables are case sensitive

'''
a=13
print(a)
print(type(a))
'''
'''
b=8.5
print(b)
print(type(b))
'''
'''
c='python'
print(c)
print(type(c))
'''
'''
d=True
print(d)
print(type(d))
'''
#input(label):It is used to get the data from the user
'''
a=bool(input("enter value: "))
print(a)
print(type(a))
'''
#Bool ->it consider only True or false
#we can write different different values that is called as dynamic values
#default function
'''
===2.Non primitive data types====
In single container we can store multiple vales

4 types
#1.list
#2.tuple
#3.set
#4.Dictionary

====1.List====
-it is a collection of values
-in single container we can pass n number of values
-List should be declare -[1,2,3.4,'python','Bhaskar',True]
-List is a mutable object -we can modify
'''
'''
li=[12,23,4.5,'Python',True]
print(li)
print(type(li))
'''
#position -0
#length   -1
#len() -It is used to find how many values present in the list
'''
li=[12,2,3,4,5.7,'Bhaskar','python',True]
print(li[7])
print(type(li[7]))
print(len(li))
'''
#list methods ->predefined functions

#1.append() -it is used to add one more value end of the list
  #list.append(value)
'''
li=[1,2,3,4,5]
li.append('python')
li.append('Bhakar')
print(li)
'''
#2.extend() -it is used to merge 2 lists -add one more value end of the value
 #list1.extend(list2)
'''
li1=[1,2,3,4,5]
li2=[6,7,8,9,10]
li1.extend(li2)
print(li2)
'''
#3.insert() -it is used to add one more value any where
   #list.insert(where[position],value)
'''
li=[1,2,3,4,5,6]
li.insert(3,'python')
li.insert(0,'Bahskar')
print(li)
'''
#4.pop() -it is used to delete particular value based on the position
 #list.pop(position)
'''
li=[21,12,34,56,73,45]
li.pop(3)
print(li)
'''
#5.remove() -it is used to delete particular value based on the value
 #list.remove(value)
'''
li=[12,45,12,76,34,87,98]
li.remove(12)
print(li)
'''
#6.sort() -it is used to make ascending order
 #list.sort()
'''
li=[43,23,12,35,67,89,34,1,2,4,35]
li.sort()
print(li)
'''
#7.reverse() -it is used to make reverse
 #list.reverse()
'''
li=[1,2,3,4,5,6,7,8,9,10]
li.reverse()
print(li)
'''
#index() -it is used to find the position based on the value
 #list.index(value)
'''
li=[1,2,76,3,4,34,56,76]
x=li.index(76)
print(x)
'''
#max(),min(),sum()
'''
li=[1,2,3,4,5]
print(max(li))
print(min(li))
print(sum(li))
'''
#count() -it is used to check the value how many times present in the list
 #list.count(value)
'''
li=[1,2,3,4,1,1,6,6,1,3,5,7,8]
x=li.count(6)
print(x)
'''
'''
=======2.Tuple====
-it is a collection of values
-in single container we can pass n number of values
-tuple should be declare -(1,2,7.8,'python',True)
-tuple is a immutable object -we cant modify
'''
'''
t=(1,2,3,'python','bhaskar',True)
print(t)
print(type(t))
'''
'''
#max(),min(),sum()
t=(1,2,3,4,5)
print(max(t))
print(min(t))
print(sum(t))
'''
#index() -it is used to find the position based on the value
 #tuple.index(value)
'''
t=(12,23,45,67,46,78,98)
y=t.index(78)
print(y)
'''
#count()
'''
t=(1,2,3,4,1,1,1,1,1,2)
y=t.count(1)
print(y)
'''
#packing() =tuple

#unpacking() -In every single value assign one individual variable
'''
t=(1,2,3,4,5,6,7,8,9)
_,*b,c,d,e=t
#print(a)
print(b)
print(c)
print(d)
print(e)
''
#Rest operator - * -rest of all the values 
#              -return as a list -[]
#Null statement =>   _  =>skip the values
#                       -empty statement

#unpacking() :In every single value assign one individual variable
'''
t=(1,2,3,4,5,6,7,8,9,10)
,,c,d,*e=t
#print(a)
#print(b)
print(c)
print(d)
print(e)
'''
#Rest operator:* =>rest of all values
#                =>it will return as a list-[]
#Null statement  =_ =>it skip the values
#                   =>empty statement
'''
===3.set====
-it is a collection of values
-in single container we can store multiple values
-set should be declare -{1,2,3,'python',True}
-set is a mutable object -we can modify
-sets are unorder collections
-sets not allows duplicate values
'''
'''
s={10,2,3,45,5,63,1,2,3}
print(s)
print(type(s))
'''
#1.add() :it is used to add one more value end of the set
 #set.add(value)
'''
s={1,2,3,4,5,6}
s.add('python')
s.add('Bhaskar')
print(s)
'''
#2.clear():it is used to make empty set
 #set.clear()
'''
s={1,2,3,4,5,67,34,56,76}
s.clear()
print(s)
'''
#3.discard() :it is used to delete particular value based on the value
 #set.discard(value)
'''
s={12,34,56,45,78,96,27}
s.discard(56)
print(s)
'''
#4.difference():it takes 2 sets -it takes only one set difference -unmatched values
'''
set1={1,2,3,6,4,5,9}
set2={1,2,23,56,6,7,8}
res=set1.difference(set2)
print(res)
'''
#5.symmetric_difference():it takes 2 sets -it takes two sets difference -unmatched values
'''
set1={1,2,34,5,6,7}
set2={1,2,9,10,56,32}
res=set1.symmetric_difference(set2)
print(res)
'''
#6.intersection():it takes more than 2 sets,common values it will return
'''
set1={1,2,3,56,23,8,10}
set2={1,2,10,23,6,7,8}
set3={1,2}
res=set1.intersection(set2,set3)
print(res)
'''
'''
====4.Dictionary=====
-dict is a colection of key and value pair
'name':'bhaskar'
-dict should be declare -{}
-dict also mutable object -we can modify

{'key':value,'key':value,'key':value}

'''
'''
obj={1,2,3,4,5}
print(obj)
print(type(obj))
'''
'''
obj={}
print(obj)
print(type(obj))
'''
'''
obj={
    'name':'bhaskar',
    'email':'bhaskar@',
    'mobile':862373672,
    }
print(obj)
print(type(obj))
'''
#get() :it is used to get particular value based on the key
 #dict.get(key)
'''
obj={
    'name':'bhaskar',
    'emial':'bhaskar@',
    'mobile':86376322,
    }
print(obj.get('mobile'))
print(obj.get('name'))
'''
'''
obj={
    'name':['bhaskar','madhu','chinni','moorthy'],
    'email':'bhaskar@',
    'mobile':86376322,
    }
print(obj)
'''
'''
obj={
    'name':['bhaskar','madhu','chinni','moorthy'],
    'email':'bhaskar@',
    'mobile':86376322,
    }
li=obj.get('name')
print(li[3])
'''
'''
'''
obj={
    'name':'bahskar',
    'email':'bahskar@',
    'mobile':876271621,
    }
print(obj)
'''
#1.add() -it is used to add one more key and value pair
 #dict['key']=value
'''
obj={
    'name':'bhaskar',
    'emial':'bhaskar@',
    'mobile':863726786,
    }
obj['city']='Vizag'
obj['state']='AP'
print(obj)
'''
#2.pop() -it is used to delete particular value based on the key
 #dict.pop(key)
'''
obj={
    'name':'bhaskar',
    'emial':'bhaskar@',
    'mobile':863726786,
    }
obj.pop('name')
obj.pop('mobile')
print(obj)
'''
#3.update() -it is used to update particular value based on the key
 #dict.update({'key':value})
'''
obj={
    'name':'bhaskar',
    'email':'bhaskar@',
    'mobile':863726786,
    }
obj.update({'name':'Moorthy'})
obj.update({'email':'Moorthy@'})
print(obj)
'''
'''
=====Operators====
operators are the symbols todo some mathematical or logical operations

5 types
#1.Arithmetic operator
#2.comparision operator
#3.logical operator
#4.membership operator
#5.identity operator

====1.Arithmetic operator===
Mathematical calculations
+,-,,/,*,%
'''
'''
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(a**b)
print(4%2)
print(6%2)
print(7%2)
#even remainder by 2 =0
#odd remainder by 2  =1
'''
'''
===2.comparision operator===
-it is used to compare the values
-it will return as a boolean
<,<=,>,>=,!=,==
'''
'''
a=100
b=200
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a!=b)
'''
#equal -it is used to check the value and data type also
'''
x=10
y=10
print(x==y)
'''
'''
====3.logical operator====
and -&& , or -||

and =if both operators are true -condition becomes true
or  =if any one operators are true -condition becomes true
'''
'''
x=100
y=200
z=300

print(x<=100 and y>=200 and z>=300)
print(x<100 or y>200 or z<300)
'''
'''
=====4.Membership operator=====
-it is used to check the sequence
-it will return as a boolean
-in,not in
'''
'''
x='hello'
print('h' in x)
print('h' not in x)
print('H' in x)
print('H' not in x)
'''
'''
li=['a','b','c','d','e']
print('a' in li)
print('A' in li)
print('A' not in li)
'''
'''
t=('a','b','e','d')
print('a' in t)
print('a' not in t)
'''
'''
===5.identity operator===
-it is used to check the memory location
-it will return as a boolean
-is,is not
'''
'''
x=10
y=20
print(x is y)
print(x is not y)
'''
'''
x=10
y=20
x=y
print(x is y)
'''


