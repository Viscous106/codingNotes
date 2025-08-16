###Python notes###

###types of data
a1,a2,a3,a4,b1,b2,c1,c2,d1,d2,e1,e2,f,g=3,4.5,4,5,'yash','virulkar',{1,2,3,4},{3,6},True,False,[1,2,4],[2,6],'0123456789','----python----'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='0123456789'
'''
print(a1,type(a1),a2,type(a2),b1,type(b1),b2,type(b2),c1,type(c1),c2,type(c2),d1,type(d1),d2,type(d2),e1,type(e1),e2,type(e2),f,type(f),g,type(g),sep='\n')
'''
###calculation operators
'''
print('addition',a1+a2,'subtraction',a1-a2,'multiplication',a1*a2,'division',a1/a2,'modulus',a1%a2,'floor devision',a1//a2,'catenation',b1+" "+b2,'union',e1+e2,'exponential',a2**a1,sep='\n')
'''
###relational operators
'''
print('a1>a2',a1>a2,'a2>a1',a2>a1,'a2>=a1',a2>=a1,'a1=a2',a1==a2,'a1!=a2',a1!=a2,'a1*1.5=a2',(a1*1.5)==a2,sep='\n')
circular swap of a1, a2, a3
'''
'''
a1, a3, a4 = a3, a4, a1
###circular swap of a1, a2, a3
print(a1,a3,a4)
'''
###logical operators
'''
print('d1 and d2',d1 and d2,'d1 or d2',d1 or d2,'not d1',not d1,sep='\n')
'''

###operation on strings
#taking individual letters
'''
print(b1[0],b1[1],b1[2],b1[3],sep='\n')
taking letter from b1[1] to b1[3]
print(b1[1:4])
print(int(f[3])*(int(f[7])))#first convert to int then operatiion or else it eill give string operations
print(b1>b2)#smaller will come first in alphabetical order
print(b1[-4],b1[-3],b1[-2],b1[-1])#negative indexing principle
print('lenght of b1=',len(b1))
print(b1[:-2])#slicing the string from start to second last letter
print(b1[:3]+ b1[::-1]) #palindrominator
#del a1   #deletes the variable
'''
'''    
a+=1#increment (a=a+1)
a-=1#decrement (a=a-1)
a*=2#multiply  (a=a*2)
a/=2#divide    (a=a/2)
a1 **=2#exponential (a=a**2)
print('it\'s a beautiful day')#to print 's in the string
print('My name is yash.\tI\'m studying at IITM')#\t is used to give tab space
print('My name is yash.\nI\'m studying at IITM')#\n is used to give new line
'''

###string methods
'''
print(b1.capitalize())#capitalizes first letter
print(b1.title())#capitalizes first letter of each word
print(b1.upper())#capitalizes all letters
print(b1.lower())#lowercase all letters
print(b1.swapcase())#swaps case of all letters
print(b1.replace('y','Y'))#replaces y with Y
print(b1.find('y'))#finds index of first occurrence of y
print(b1.count('y'))#counts number of occurrences of y
print(b1.islower())#checks if all letters are lowercase
print(b1.isupper())#checks if all letters are uppercase
print(b1.isalpha())#checks if all letters are alphabets
print(b1.isalnum())#checks if all letters are alphanumeric
print(b1.isdigit())#checks if all letters are digits
print(g.strip('-'))#removes - from both sides
print(g.lstrip('-'))#removes - from left side
print(g.rstrip('-'))#removes - from right side
'''

###Ceaser Chipher in cryptography 
#how protect the privacy of your code you can use this code such that you can change the pattern by which the code is written and then you can decode it by using the same code

###if else elif
'''
birth_year= int(input('Enter your birth year:'))
current_year=2025
age= current_year-birth_year
if age <18:
   print('sorry you are not eligible to create an account')
elif age >=18:
   print('you are eligible to create an account')
print('thank you for using our service')#this print command is outside the if else block so it will always executeno matter what the condition is'''

###import library 

###import math
'''
import math
print(math.exp(2))
print(math.log(2))
print(math.log10(2))
print(math.sqrt(2))
print(math.factorial(5))
print(math.floor(2.5))#GIF
print(math.ceil(2.5))#LIF
print(math.pi)
print(math.e)
print(math.tan(math.pi/4))
print(math.degrees(30))#converts radian to degree
print(math.radians(30))#converts degree to radian
print(math.hypot(3,4))#hypotenuse
''' 


###import random
'''
import random
print(random.randint(1,6))#random number between 1 and 6 #can also use random.randrange(1,6) which will give 1 to 5
print(random.uniform(1,10))#random float between 1 and 10
print(random.random())#random number between 0 and 1
print(random.choice([1,2,3,4,5,6,7,8,9,10]))#random choice from the list
print(random.sample([1,2,3,4,5,6,7,8,9,10],3))#random sample of 3 from the list
'''
###coin toss
'''
a=random.random()
if a<0.5:
    print('head')
elif a>0.5:
    print('tail')
else:
    print('draw')
'''

###import calander
'''
import calendar as c
year=int(input('Enter the year:'))
month=int(input('Enter the month:'))
print(c.month(year, month))#prints the calendar of the month of the year
print(c.calendar(year))#prints the calendar of the year
'''
#alternate way
'''
from calendar import *
year=int(input('Enter the year:'))
from calendar import *
month_=int(input('Enter the month:'))
print(month(year, month_))
'''

###while loop
'''
year=int(input('print my birth year:'))
while (year!=2006):
   print('you are wrong. Try again.') 
   year=int(input('print my birth year:'))
print('seems like you remember it!!')
'''
###factorial of a number using while loop
'''
num=int(input('Enter a number to find its factorial:'))
fact=1
while (num!=0):
    fact*=num
    num=num-1

print('factorial of the number is:',fact)
'''
###for loop 
#sum of first n natural numbers
'''
sum=0
for i in range((int(input('Enter a number:')))+1):   # for natural num +1 as it starts with 0 as we know int starts from 0 
    sum+=i
print('sum of the numbers is:',sum)
'''
#(start (include) , stop (not include), step/common difference)
'''
for i in range(1,11,2): 
    print(i)
'''
#reverse order
'''
for i in range(10,-1,-1):
    print(i)
'''
###for each (str concept)
'''
country='India'
for something in country:#something can be anything , basicaly in int it prints 01234... in given range similarly here it prints country[0],country[1]....
    #print(something)
    #print(something,end=' ')#end=' ' is used to print in same line with space
'''

'''
d=int(input('Enter a date: '))
m=int(input('Enter a month: '))
y=int(input('Enter a year: '))
print('The date is:',end='')
print(d,m,y,sep='/')#sep='/' is used to print with / in between
'''
###use of f'' in print
'''
num=int(input('Enter a number: '))
for i in range(1,11):
    print(num,'x',i,'=',num*i)
    #print(f'{num} x {i} = {num*i}')#f-string formatting #use :.nf to print float upto n decimal places 
    #print('{0} x {1} = {2}'.format(num,i,num*i))#using format method
    #print('%d x %d = %d' % (num,i,num*i))#using % operator
'''
#nested for loop
#use of matrix
'''
die1='123456'
die2='123456'
for i in die1:
    if i=='1':
        for j in die2:
            print(i,j,sep=' ',end=' | ')#sep=' x ' is used to print with x in between and end=' | ' is used to print | at the end of each combination
        print()
    elif i=='2':
        for j in die2:
            print(i,j,sep=' ',end=' | ')
        print()
    elif i=='3':
        for j in die2:
            print(i,j,sep=' ',end=' | ')
        print()
    elif i=='4':
        for j in die2:
            print(i,j,sep=' ',end=' | ')
        print()
    elif i=='5':
        for j in die2:
            print(i,j,sep=' ',end=' | ')
        print()
    elif i=='6':
        for j in die2:
            print(i,j,sep=' ',end=' | ')
        print()
'''
###break and continue
'''
EMAIL=input('Enter your email: ')
for i in EMAIL:
    if (i=='@'):
        break 
        #continue
    print(i,end='')
else:
    pass #5star do nothing
'''

###list fxns:
'''
e1.sort()#sorts the list in ascending order
e1.append('yash')#adds yash to the end of the list
e1.append(9) #adds 9 to the end of the list
e1.reverse()#reverses the list
e1.insert(2,'virulkar')#inserts virulkar at index 2
e1.remove('yash')#removes yash from the list
e1.pop(2)#removes the element at index 2
print(e1)
'''
#matrix of by lists:
'''
e3=[]
e3.append(8)
e3.append(e2[0])
e3.append(e1[1])
e2.append(7)
e=[]
e.append(e1)
e.append(e2)
e.append(e3)
print(e)
'''
#m2:
'''
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M[0][0])#prints 1
print(M[1][1])#prints 5
M[0][0]=10#changes 1 to 10
print(M[0][0])
'''
'''
L=list(range(1000000))
print(L[10])#prints first 10 elements
if 'YASH' in L:
    print('true')
else:
    print('false')
S=set(range(1000000))#set is unordered collection of unique elements
#Set is faster than list for searching
#Set takes more memory than list
#Set is mutable, but cannot be indexed or sliced like lists i.e we cannot access elements using index {s[0]}
#Set is used to perform mathematical set operations like union, intersection, difference, etc.
#Set is used to remove duplicates from a list
'''
'''
###tuple
t=(1,2,3,4,5,6,7,8,9,10)
#t[0]=10 #tuples are immutable, so we cannot change the value of an element
print(t[0])#prints 1
#tuple is used just because it is movable and less memory consuming than list.
'''
'''
###Intro to functions:
def add(a,b):
    print(a+b) 
add(2,3)#calls the function and returns 5
'''
'''
###isinstance:
x = [1, 2, 3]
print(isinstance(x, list))    # True
print(isinstance(x, dict))    # False
'''
'''
###hasttr:
class Dog:
    def bark(self):
        pass

dog = Dog()
print(hasattr(dog, "bark"))   # True
print(hasattr(dog, "run"))    # False
'''
###Dictonary:
'''
dict={
    "key" : "value",
    "name" : "Yash",
    "cgpa" : "7.9",
}
print(dict["name"])#prints Yash
print(dict.get("cgpa"))#prints 7.9
print(list(dict.keys()))
print(list(dict.values()))#prints ['Yash', '7.9']
print(list(dict.items()))#prints [('key', 'value'), ('name', 'Yash'), ('cgpa', '7.9')]
print(list(dict.get("name"))) #prints ['Y','a','s','h']
print(dict.get("name"))#prints Yash
#use of dict.get:
#print(dict["name2"])-- gives error
print(dict.get("name2"))#prints none
'''
'''
#Nested loop for dic:
student={
    "name":"Yash Virulkar",
    "subject":{
        "phy":90,
        "chem":50,
        "maths":100
    }
}
print(student["subject"])
print(student["subject"]["chem"])
'''
###matrix mulpn:
#M1 classic
'''
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]
r4=[1,2,1]
r5=[6,2,3]
r6=[4,2,1]
M1=[]
M2=[]
M1.append(r1)
M1.append(r2)
M1.append(r3)
M2.append(r4)
M2.append(r5)
M2.append(r6)   
M3=[[0,0,0],[0,0,0],[0,0,0]]
dim=3  #assuming both matrices are square matrices
for i in range(dim):
    for j in range(dim):
       for k in range(dim):
            M3[i][j]=M3[i][j]+M1[i][k]*M2[k][j]
print(M3)
'''
#m2 using numpy:

#import numpy as np
'''
M1=np.array([[1,2,3],[4,5,6],[7,8,9]])
M2=np.array([[1,2,1],[6,2,3],[4,2,1]])
M3=np.dot(M1,M2)
print(M3)
'''
#M3 using Function:
'''
def row_inp():
    
    #r1=[1,2,3]
    #r2=[4,5,6]
    #r3=[7,8,9]
    #r4=[1,2,1]
    #r5=[6,2,3]
    #r6=[4,2,1]
    
    r1=[int(input()),int(input()),int(input())]
    r2=[int(input()),int(input()),int(input())]
    r3=[int(input()),int(input()),int(input())]
    r4=[int(input()),int(input()),int(input())]
    r5=[int(input()),int(input()),int(input())]
    r6=[int(input()),int(input()),int(input())]
    
    a=[r1,r2,r3]
    b=[r4,r5,r6]
    dim=len(a)  #assuming both matrices are square matrices
    c=[[0,0,0],[0,0,0],[0,0,0]]  #initializing the result matrix with zeros
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                c[i][j] = c[i][j]  + a[i][k] * b[k][j]
    return c
print(row_inp())
'''
'''
###lambda function:
#used for def fxn of just one lines
add = lambda x, y: x + y
print(add(int(input()), int(input())))  # Output: 5
'''
#####Recursion
'''
#This sorts out a list:
def mini(L):
    mini=L[0]
    for i in L  :
        if (i<mini):
            mini=i
    return mini
def sort(L):
    if L==[] or  len(L)==1:
        return L
    m=mini(L)
    L.remove(m)
    return [m]+sort(L) #this is recursion
print(sort([1,4,5,3,2]))
'''
###Reminder to make notes for binary search :
#Also use recursion:












######Exception Handeling:
'''
a=int(input())
b=int(input())#If input is 0 it gives Zerodivision error
try:
    f=open('demo.txt','r')
    c=a/b
    print(c)
    print(d)#It gives the NameError
except ZeroDivisionError:
    print("Denominator can't be 0")
except NameError:
    print("Sorry the variable is not present")
except:
    print('Something went wrong!!')
finally:#Even if error occurs above the code will break fr but this block i.e. the finally block always gets excecute
    f.close()
    print('Finally block got executed')
'''

#######How to raise an exception:
'''
age=int(input())
if age<18:
    raise Exception('You are underage')#now an error will raise every time an age under 18 is entered
'''

##Class and Objects:
'''
class Student:
    roll_no = None
    name     = None

s0 = Student()
s0.roll_no=10613
s0.name='Yash Virulkar'
print(s0.roll_no,s0.name)
'''
#Better way to write class oriented 
'''
class Student:
    fullname="anonymous"#In case both obj and class attr are present obj attr is given preff . if only when obj attr is absent the class attr executes
    collegeName='IITM' #Class attr i.e. common for all
    def __init__(self,roll_no,fullname):#We have to use __init__ only#IT is also called as constructor
        count=0#It belong to Student
        self.roll_no=roll_no #Obj attr (specific for the obj)
        self.name=fullname
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("college Name:",self.collegeName)
s0 = Student('10613','Yash Virulkar')
s0.display()

s1=Student('10100','Nikhil')
s1.display()

'''
###Static Method:
#This method is used in case you dont want to use self 
#Used of class only not obj
'''
class Lol:
    @staticmethod #this is a decorator used to tell compilor that we are using
    def laugh():
        print('I am laughing out my stomach')
'''


###ABSTRACTION:
#show only the neccessary stuf and hide useless 
#Def:Hiding the implementation etail of a class and showing the essential features to the user
'''
class car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=True
    def start(self):
        self.acc=True
        self.clutch=True
        print('Car started')
car0 = car()
car0.start()#Here output has no mention of the brake oor acc behind the scene

'''

###Encapsulation:
#Def :Wrapping data and function into a single unit object 
'''
class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    def detail(self):
        print('Account Num:',self.acc)
        print('Balance:',self.bal)
    def debit(self,deb):
        self.deb=deb
        print('The amount debited is',self.deb)
        print("The amount after debit is:", (self.bal-self.deb))
    def credit(self,cre):
        self.cre=cre
        print('The amount credited is',self.cre)
        print("The amount after credit is:", (self.bal-self.cre))
acc1=Account(10000,12345)
acc1.detail()
acc1.debit(400)
acc1.credit(700)
'''

#del s0 #Deletes the object
#del s0.name#deletes the obj property

###For other languages the class can be made private but in python it can only be made private (like)  just add '__' before variable to make it private

###Inheritance:
#When one class derives the property & meth of another class
'''
class car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print('Car started')

class toyotaCars(car):#all the fxns of class car are inherited now
    def __init__(self,name):
        self.name=name
car1 = toyotaCars("fortuner")
car2 = toyotaCars("prius")
print(car1.name,car1.start())
print(car2.name,car2.start())
'''

#there is a @classmethod used to change directly the class attr#for details chatgpt

###dunder function:
#ex:use __add__ to make a fxn for add complex num

##intro to numpy:

import numpy as np
a=np.array(0)
b=np.array([0,1,2])
print(a,a.ndim)#ndim gives dimension of matrix
print(b,b.ndim)
