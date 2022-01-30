'''
x="awesome"
def myfunc():
    x="fantastic"
    print("python is "+x)
myfunc()
print("python is "+x)

print("----*----")
def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is "+x)


y = "awesome"

def myfunc():
  global y
  x = "fantastic"

myfunc()

print("Python is " + y)

import random
print(random.randrange(1,10))

a="Hello,World"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H","J"))
print(a.split(","))


txt = "The rain in Spain stays mainly in the plain"
c = "ain" in txt
print(c)

age=19
txt="My name is Simran , I am {}"
print(txt.format(age))


print(bool("Hello"))
print(bool(17))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



t=200
print(isinstance(t,int))



x=200
y=300
print(x+y)

thislist=["apple","banana"]
print(thislist)
#print(thislist[1])
for x in thislist:
    print(x)
for apple in thislist:
    print("yes,'apple' is in the fruits list")
print(len(thislist))
thislist[0]="simmu"
print(thislist)
thislist.append("orange")
print(thislist)

thislist.insert(1,"simran")
print(thislist)


print("---tuple--")
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

'''
x="banana"
for x in "banana":
    print(x)
fruits=["banana","apple","cherry"]
for x in fruits:
    print(x)
    if x=="apple":
        break



for i in range(2,3,4):
    print(i)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


def my_function(fname):
    print(fname +" Simoliya")
my_function("Simran")
my_function("Sim")

def tri_recursion(k):
    if(k>0):
        result=k + tri_recursion(k-1)
        print(result)
    else:
        result =0
    return result
print("\n\n recursion example")
tri_recursion(6)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#p1=Person("simran",19)
#print(p1.name)
#print(p1.age)
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1=Person("simran",19)
p1.myfunc()


print("--iterators--")
tuple =("apple","banana")
myit=iter(tuple)
print(next(myit))
print(next(myit))



class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumber()
myit=iter(myclass)
print(next(myit))
print(next(myit))


class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumber()
myiter=iter(myclass)
for i in myiter:
    print(i)


print("--modules--")
import mymodules
mymodules.greetings("simran")
a=mymodules.person1["country"]
print(a)

print("--OR--")
import mymodules as md
md.greetings("simran")
a=md.person1["country"]
print(a)

import platform
x=platform.system()
print(x)

x=dir(platform)
print(x)

print("--datetime--")
import datetime
x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))

print("--math--")
import math
print(math.sqrt(64))
print(math.pi)
x=2.4
print(math.ceil(x))

print("--JSON--")
import json
x={
    "name":"Simran",
    "age":19,
    "country":"India"
    }
y=json.dumps(x)
print(y)



print("--re--")
import re
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
print("The first white-space character is located in position:", x.start())


print("--input in python--")
username=input("enter my name-")
print("username is: "+username)


age=input("Enter age-")
txt="my age is {} years"
print(txt.format(age))




print("--file handling--")
f=open("simmu.txt","rt")
print(f.read())
print("--OR--")
print(f.read(5))



print("--numpy--")
import numpy
arr=numpy.array([1,2,3])
print(arr)






