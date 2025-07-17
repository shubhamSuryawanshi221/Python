'''
=======Loops=======
It execute repetedly untill the condition is true/false.
#2.Types are there
#1.for loop
#2.While loop

========1.For loop========
It is a single line expression/one line statement
it iterate each and every values

for loop_name in expression:
   statement

for => Key name
loop_name => anything
in => Key name
expression => range(start,end,step)

range (1,20,1) => (1,2,3,4,5..........19)
'''
'''
for i in range(1,10):
    print(i)
'''

'''
for i in range(1,10,2):
    print(i)
'''

'''
for j in range(10,1,-1):
    print(j)
'''

'''
for i in range(1,10,1):
    if(i%2==0):
        print(i)
'''

'''
for i in range(1,10,1):
    if(i%2==1):
        print(i)
'''

'''
for j in range(10,1,-1):
    if(j%2==1):
        print(j)
'''

'''
for i in range(1,20,1):
    if(i%2==0):
        print(i,'I am even')
    else:
         print(i,'I am odd')
'''

'''
li=[12,23,45,34,56,78,95,67]
for i in range(0,len(li),1):
    print(i)
'''

'''
li=[12,23,45,34,56,78,95,67]
print(li)
'''

'''
li=[12,23,45,34,56,78,95,67]
for i in range(0,len(li),1):
    print(li[i])
'''

'''
#find Odd Values
li=[12,23,45,34,56,78,95,67]
for i in range(0,len(li),1):
    if(li[i]%2==0):
        print(li[i])
'''

'''
#Find Even Values
li=[12,23,45,34,56,78,95,67]
for i in range(0,len(li),1):
    if(li[i]%2==1):
        print(li[i])
'''

'''
li=[12,23,45,34,56,78,95,67]
for i in li:
        print(i)
'''

'''
=====2.While Loop====

it is starting control loop-condition started starting only
it will execute repetedly untill the condition is false

starting_value
while(ending_value):
     statement
     step
'''
'''
#Even values
i=1
while(i<=20):
    print(i)
    i=i+1
'''
'''
i=1
while(i<=20):
    if(i%2==0):
     print(i)
     i=i+1
'''

'''
1<=20 -> True
2<=20 -> True
3<=20 -> True

20<=20 -> True
'''

#Quetion for HW

#in between 1 to 20 find sum of all even values
#in between 1 to 20 find sum of all odd values























    








































        
        
        









































        
