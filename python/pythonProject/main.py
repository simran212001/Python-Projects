# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram =  ram
#     def config(self):
#         print('Config is', self.cpu , self.ram)
#
# com1 = Computer('i5',16)
# com2 = Computer('Ryzen3',8)
#
# # Computer.config(com1)
# # Computer.config(com2)
#
# com1.config()
# com2.config()
#
# a=416378
# a.bit_length()
# print(a)
#
# class Computer:
#     pass
# c1 = Computer()
# c2 = Computer()
# print(id(c2))
# print(id(c1))
#
# class Computer:
#     def __init__(self):
#         self.name = 'Simran'
#         self.age = 20
#     def update(self):
#         self.age = 20
#
#     def Compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
# c1 = Computer()
# c2 = Computer()
# c1.name = 'Lakshya'
# c1.age = 21
# c1.update()
# print(c1.name)
# print(c1.age)
# print(c2.name)
# print(c2.age)
# if c1.Compare(c2):
#     print('They are same')
# else:
#     print("They aren't same" )

# class MyComplexNumber:
#     def __init__(self,real= 0,imag=0):
#         print('My complex number')
#         self.real_part = real
#         self.imag_part = imag
#     def displayComplex(self):
#         print('{0}+{1}j'.format(self.real_part,self.imag_part))
# c1 = MyComplexNumber(2,7)
# c1.displayComplex()
#
# c2= MyComplexNumber(3,4)
# c2.new_attribute = 8
# print((c2.real_part,c2.imag_part,c2.new_attribute))
# del c1.real_part
# print(c1.imag_part)


# -------------ARRAYS----------
# arr = [1,23,4,6,7,8]
# print(arr)
# print(arr[5])
# Name = ["Simran", "Simoliya"]
# print('1st element of Name array is -', Name[0])
# Name.append(8)
# print(Name)
#
# Alpha = ['A','B','C','D','E','F']
# print('Length of array Alpha is -',len(Alpha))
# del Alpha[3]
# Alpha.remove('B')
# Alpha.pop(1)
# print(Alpha)
#
# Fruits = ['Apple','Banana','Mango']
# Fruits[1] = 'Guava'
# print(Fruits)
# # slicing an array
# print(Fruits[0:1])
#
# print('Concating 2 arrays using +')
# Concat = [1,2,3,4,5]
# Concat = Concat + [6,7,8]
# print(Concat)
#
# repeat = ['a']
# repeat = repeat*5
# print(repeat)
#
# # multidimensional array
# multd = [[1,2],[1,3],[1,4]]
# print(multd[0])
# print(multd[0:2])
# print(multd[1][1])
# print(multd[1][0])
#
# from array import *
# vals = array('i',[1,2,4,5,-7,8])
# vals.reverse()
# for i in range(6):
#     print(vals[i])
# print('-------OR---------')
# for e in vals:
#     print(e)
#
#
# print('----------------new aray with the same elemnts------------------')
# newArr = array(vals.typecode , (a for a in vals))
# for e in newArr:
#     print(e)
# print('---------------Square of the elements of newArr ----------------')
# newArr = array(vals.typecode , (a*a for a in vals))
# print(newArr)
# for e in newArr:
#     print(e)
#
# print('---------------ask a user to enter the valus in an empty array----------')
# from array import *
# arr = array('i',[])
# n = int(input('Enter the length of the array'))
# for i in range(n):
#     x = int(input('Enter the element:'))
#     arr.append(x)
# print(arr)
#
# print('----------------Search an element-------------')
# s = int(input('Enter the value you want to seach:'))
# for i in range(len(arr)):
#     if s == arr[i]:
#         print("The index number for this value is:",i)
# print("---------or--------")
# k=0 #index number
# for e in arr:
#     if e == s:
#         print(k)
#         break
#     k+=1
#
# print('-----Seach with functions----------')
# print(arr.index(s))
#
# from numpy import *
# ar = array([1,2,3,1,2,3])
# print(ar)
# print(ar.dtype)
# arr2 = array([1,2,3,4.0,5],int)
# print(arr2)
# print('-----------------"linspace"-------------------')
# arr3 = linspace(0,2,5)
# print(arr3)
# print("--------------------'ARANGE'------------")
# arr4 = arange(1,15,2)
# print(arr4)
# print('---------------------"logspace"--------------')
# arr5 = logspace(1,40,3)
# print(arr5)
# print('---------------------"zeros"--------------')
# arr6 = zeros(6)
# print(arr6)
# print('---------------------"ones"--------------')
# arr7 = ones(4)
# print(arr7)
# print('---------------------"coping array"--------------')
# a = array([1,2,3,4,5])
# b = a
# print(a,b)
# print(id(a),id(b))
#
# b = a.view()
# a[2]=10                 #value change in both arrays ...means they are depending on each other
# print(a,b)
# print(id(a),id(b))      #different for both the arrays
#
# b = a.copy()
# a[3] = 100              #value change in only a not in b ...means they are not depending
# print(a,b)
# print(id(a),id(b))
#
# print('---------------------"Multi dimensional"----------------')
# multd = array([
#     [1,2,3,4],
#     [1,2,3,4]
# ])
# print(multd)
# print(multd.dtype)
# print(multd.size)
# print(multd.ndim)
# print(multd.max())
# print(multd.flatten())
# print(multd.shape)
# print(multd.reshape(2,3))
# print(multd)
#
# print('---------------"Matrices/diagonal matrices"-------------------')
# from numpy import*
# arr = array([
#     [1,2,3],
#     [4,5,6]
# ])
# m = matrix(arr)
# print(m)
# print(m.size)
# A = matrix('1 2 3; 4 5 6; 7 8 9')
# print(diagonal(A))
# B = matrix('1 2 3; 4 5 6 ; 7 8 9')
# C = A+B
# print("Sum of two matrices",C)
# D = A*B
# print("Multiplication of two matrices",D)
#
# print('-----------------File Handling---------------')
# f = open('MyData','r')
# print(f)
# print(f.read())
# f1 = open("abc",'w')
# f1.write("Something")
# f1.write(" \nhello")
# f1 = open('abc','a')
# f1.write('\nmobile')
# for data in f:
#     # print(data)
#     f1.write(data)
#
# f3 = open('image.jpg','rb')
# print(f3.readline())
# for i in f3 :
#     print(i)
# f4 = open('image2.jpg','wb')
# for i in f3:
#     print(i)

# print('--------------"Keywords and identifiers"-----------------')
# #True False
# print(2==2)
# print(3>3)
# # None
# print(None == 0)
# print(None == False)
# print(None == [])
# print(None == None)
# def a_void_function():
#     a =1
#     b = 2
#     c = a+b
#     # print(c)
# x = a_void_function()
# print(x)
# # print(c)
#
# # and , or , not (boolean)
# print(True and True)
# print(True and False)
# print(False and False)
# print(True or True)
# print(not True)
#
# # as
# import math as m
# print(m.cos(m.pi/2))
#
# # assert
# assert 5>4
#
# # break
# for i in range(1,10):
#     if i == 4:
#         break
#     print(i)
#
# # continue
# for i in range(1,10):
#     if i == 4:
#         continue
#     print(i)
#
# # class
# class ExampleClass:
#     def function1(self):
#         print("Function1 excuting......")
#     def function2(self):
#         print("Funcion2 excuting..........")
# obj1 = ExampleClass()
# obj1.function1()
# obj1.function2()
#
# # def
# def function_name(value):
#     pass
# function_name(2)
#
# # del
# a=2
# print(a)
# del a
# print(a)

# if else
# num = 4
# if num == 1:
#     print('One')
# elif num == 2:
#     print('Two')
# else:
#     print('Something else')
#
# # try ..raise..catch..finally
# try:
#     x=9
#     raise ZeroDivisionError
# except ZeroDivisionError:
#     print('Division cannot be performed')
# finally:
#     print('Execution successfully')
#
# # from
# import math
# from math import cos
# print(cos(90))
#
# # global
# globvar  = 10
# def read1():
#     print(globvar)
# def write():
#     global globvar
#     globvar = 5
# def write2():
#      globvar = 15      #local variable
# read1()
# write()
# read1()
# write2()
# read1()
#
# # in , is lambda
# a = [1,2,3,4]
# for i in range(len(a)):
#     print(a[i])
# # print(1 in a)
# # print(10 in a)
# # print(True is True)
# A = lambda x: x*2
# for i in range(1,5):
#     print(A(i))
#
# # nonlocal
# def outer_function():
#     a=3
#     def inner_function():
#         nonlocal a
#         a=10
#         print('Inner Function:',a)
#     inner_function()
#     print("Outer function",a)
# outer_function()
#
# # while
# i = 0
# while i<=5:
#     print(i)
#     i+=1
# j=5
# while j>0:
#     print(j)
#     j-=1
#
# # with
# with open('example.txt','w') as my_file:
#     my_file.write('hello World!')
#
# # yield
# def generator():
#     for i in range(7):
#         # print(i*i)
#         yield i*i
# g = generator()
# for i in g:
#     print(i)
# generator()

# import speedtest
# test = speedtest.__version__
# down = test.download()
# upload = test.upload()
# print("down speed : {down}")

# import cowsay
# cowsay.daemon("hi deamon")
#
# import winsound
# f = 4000
# d = 10000
# winsound.Beep(f,d)
#
# # os  working with directory
# import os
# print(os.getcwd())          #return present directory working
# print(os.getcwdb())         #present directory working as a byte
#
# os.chdir('C:\\Users\\hp\\PycharmProjects')     # use to change directory
# print(os.listdir())                            #canbe known using listdir() method
#
# print('----------------Create new directory----------------')
# # os.mkdir('simran')
# print('--------------Rename a directory ')
# # os.rename('simran',"python by udemy")
# # os.remove(('simran.txt'))
# os.rmdir('python by udemy')
# os.chdir()

# global,local variables
# x = 'global'
# def funct1():
#     global x
#     y = 'local'
#     x = x*2
#     print(x,y)
# print(x,"-outside the function")
# funct1()
# print(x,'-inside')
#
# # local
# a = 10
# def fun():
#     a = 15
#     print(a)
# print(a)
# fun()
# print(a)
# # Nonlocal
# def outer():
#     z = "local"
#     def inner():
#         nonlocal z
#         z = " nonlocal"
#         print(z,'-in inner functio')
#
#     inner()
#     print(z,'-outer')
# outer()
#
# # global keyword
# def fun1():
#     k = 10
#     def fun2():
#         global k
#         k = 5
#     print("before calling fun2",k)
#     fun2()
#     print("after calling fun2",k)
# # print(k)
# fun1()
# print(k)

# a= 12
# def something():
#     global a
#     a = 10
#     print(a,'inside')
# print(a,'before calling fun')
# something()
# print(a,'outside')
# if we want to create local and global in same function then (use globals)
# a= 12
# def something():
#     a = 40          #local variable
#     x = globals()['a']
#     globals()['a'] = 10
#     print(a , 'inside')
#     print(x , 'x')
# print(a,'before calling fun')
# something()
# print(a,'outside')

# -------------------Iterator----------(list,tuple,string etc
# our_list = [2,43,5,7]
# it = iter(our_list)
# while True:
#     print(next(it))
#     StopIteration
# print(it.__next__())
# print(next(it))
# want to create our own iterator
# class TopTen:
#     def __init__(self):
#         self.nums = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.nums <= 10:
#             val = self.nums
#             self.nums+=1
#             return val
#         else:
#             raise StopIteration
#
# values = TopTen()
# print(next(values))
# for i in values:
#     print(i)

# -------------------- create iterator for pow of 2-----------------
# class Pow_of_Two:
#     ''' Class to implement an iterator
#         of pow of 2'''
#
#     def __init__(self):
#         self.n = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n <= 5:
#             # val = self.n
#             result = 2** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
# print(Pow_of_Two.__doc__)
# values = Pow_of_Two()
# for i in values:
#     print(i)

# #--------------------------- OR---------------
# class Pow_of_Two:
#     ''' Create a iterator for
#          pow of 2'''
#
#     def __init__(self,max = 0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             val = self.n
#             result = 2**self.n
#             self.n +=1
#             return result
#         else:
#             raise StopIteration
#
# print(Pow_of_Two.__doc__)
# values = Pow_of_Two(6)
# for i in values :
#     print(i)

# -----------------------------Infinite iterotor to return all odd numbers--------------------
#
# class Infinite_iter:
#      '''Infinite iterotor to
#      return all odd numbers'''
#
#      def __iter__(self):
#          self.n = 1
#          return self
#
#      def __next__(self):
#          val = self.n
#          self.n += 2
#          return val
#
# print(Infinite_iter.__doc__)
# values = Infinite_iter()
# # for i in values:
# #     print(i)
# n = iter(values)
#
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# ---------------------------------Inheritance-------------------
# 1 . Single Inheritance
# class A:
#     def feature1(self):
#         print("Feature1 is working")
#     def feature2(self):
#         print("Feature2 is working")
#
# class B(A):
#     def feature3(self):
#         print("Feature3 is working")
#     def feature4(self):
#         print("Feature4 is working")
#
# a1 = A()
# a1.feature1()
# a1.feature2()
#
# b1 = B()
# b1.feature2()
# b1.feature1()
# b1.feature4()
# b1.feature3()

# 2 . Multi leval Inheritance
# class A:
#     def feature1(self):
#         print("Feature1 is working")
#     def feature2(self):
#         print("Feature2 is working")
#
# class B(A):
#     def feature3(self):
#         print("Feature3 is working")
#     def feature4(self):
#         print("Feature4 is working")
#
# class C(B):
#     def feature5(self):
#         print("Feature5 is working")
# a1 = A()
# a1.feature1()
# a1.feature2()
#
# b1 = B()
# b1.feature2()
# b1.feature1()
# b1.feature4()
# b1.feature3()
#
# c1 = C()
# c1.feature2()

# 3 . Multiple inheritance
# class A:
#     def feature1(self):
#         print("Feature1 is working")
#     def feature2(self):
#         print("Feature2 is working")
#
# class B:
#     def feature3(self):
#         print("Feature3 is working")
#     def feature4(self):
#         print("Feature4 is working")
#
# class C(A,B):
#     def feature5(self):
#         print("Feature5 is working")
# a1 = A()
# a1.feature1()
# a1.feature2()
#
# b1 = B()
# b1.feature4()
# b1.feature3()
#
# c1 = C()
# c1.feature2()

# -----------------Constructor---------------
# class A:
#     def __init__(self):
#         print("in A init")
#     def feature1(self):
#         print("Feature1 is working")
#     def feature2(self):
#         print("Feature2 is working")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("in B init")
#     def feature3(self):
#         print("Feature3 is working")
#     def feature4(self):
#         print("Feature4 is working")
#
# # class C(B):
# #     def feature5(self):
# #         print("Feature5 is working")
# a1 = B()

# print('-------------------------Functions-----------------')
# def myAddition(a,b):
#     print("Performing the addition operation")
#     return a+b
# def mySubtraction(a,b):
#     print("Performing the subtraction")
#     return (a-b)
# def myMUltiplication(a,b):
#     print("Performing the multiplication")
#     return a*b
# def myDevision(a,b):
#     if b == 0:
#         print("Devision cannot possible")
#     else:
#         print("Performing the devision")
#         return (a/b)
# def myMenu():
#     print("Main Menu...")
#     print("1> Additiom")
#     print("2> Subtraction")
#     print("3> Multiplication")
#     print("4> Devision")
#     choice = int(input("Please enter the option number :"))
#     return choice
# def myCalculation():
#     choice = myMenu()
#     num1 = int(input("Enter the number 1-"))
#     num2 = int(input("Enter the number 2-"))
#     if choice == 1:
#         result = myAddition(num1,num2)
#     if choice == 2:
#         result = mySubtraction(num1,num2)
#     if choice == 3:
#         result = myMUltiplication(num1,num2)
#     if choice == 4:
#         result = myDevision(num1,num2)
#     print("Result:",result)
#
# myCalculation()

# print("------------------------Random/break------------------")
# import random as r
# rand_num = r.randrange(1,50)
# print("Any Random number b/w 1-10 is :",rand_num)
# i = 0
# while True:
#     print("Guessed number :", i)
#     if i == rand_num:
#         print("Random number has been guessed successfully")
#         break
#     i += 1
# print("End program............")

# continue
# i = 0
# for i in range(1,10):
#     if i%2 == 0:
#         continue
#     print(i)

# print("--------------------exception------------")
# try:
#     a = "200"
#     b = int(a)
#     print("I am here")
#     print(b)
# except:
#     print("Exception caught!")
#
# try:
#     a = 2
#     b = 1
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero is not possible")
#
# # ----------exception can be raised also
# try:
#     raise TypeError
# except TypeError:
#     print("TypeError caught!")
#
# # ----------try....finally--
# try:
#     print("In a try block")
#     raise TypeError
# except:
#     print("In except block")
# finally:
#     print("In finally block")

# try:
#     a = int(input("Enter the value of a :"))
#     b = int(input("Enter the value of b :"))
#     if a < 0:
#         raise TypeError
#     c = x/y
#     print("{} / {} = {}".format(a,b,c))
# except ZeroDivisionError:
#     print("Division is not possible")
# except ValueError:
#     print("The data types are not proper")
# except TypeError:
#     print("Data is not in range")
# except NameError:
#     print("The data items are not defined")

# print("----------------Exception defined by user-------------")
# class VotersEligibility(Exception):
#     def __init__(self):
#         super()
# try:
#     age = int(input("Enter the age :"))
#     print("Age is " + str(age))
#     if age < 18:
#         raise VotersEligibility
# except VotersEligibility:
#     print("age is less than 18.")
# except ValueError:
#     print("Value type is not proper")
# else:
#     print("age is equal or greater than 18.")
# finally:
#     print("End Program .........")

# from array import *
# arr = array('i', [])
# def fun(arr):
#     n = int(input("Enter the length of array : "))
#     print("N = ",n)
#     for i in range(0,n):
#         x = int(input("Enter the elements : "))
#         arr.append(x)
#     print(arr)
#     arr[n-1] = arr[n-1] + 1
#     carry = arr[n-1]/10
#     arr[n-1] = arr[n-1] % 10
# # now in case of 9 9 9 we have to increament all tha digits
#     for j in range(n-2,0):
#         if carry == 1:
#             arr[j] = arr[j] + 1
#             carry = arr[j] / 10
#             arr[j] = arr[j] % 10
#     if carry == 1:
#         arr.insert(0,1)     #insert 1 at index 0
# fun()
# for i in arr:
#     print(i)


# # ---------------------------------------OOPs Approach----------------------------------
# class myBird:
#     def __init__(self):
#         print("myBird class constructor is executing..........")
#
#     def whatType(self):
#         print("I am a Bird...")
#
#     def canSwim(self):
#         print("I can swim...")
#
# class myParrot:
#     #class attribute
#     species = "bird"
#
#     # instance attribute
#     def __init__(self,name,age):
#         print("myParrot class constructor is executing.....")
#         self.name = name
#         self.age = age
#
#     def canSing(self,thisSong):
#         return "{} can sing {} song.".format(self.name,thisSong)
#
#
# class myPenguin(myBird):
#
#     def __init__(self):
#         super().__init__()
#         print("Penguin is ready..")
#     def whoisThis(self):
#         print("I am Penguin..")
#     def canRun(self):
#         print("I can run faster..")
#
# mp1 = myParrot("MyParrot", 10)
# print(mp1.canSing('chirp'))
#
# # access class attribute
# print("mp1 is a {}".format(mp1.__class__.species))
#
# # access the instance attribute
# print("{} is {} years old ".format(mp1.name , mp1.age))
#
# pg1 = myPenguin()
# pg1.whoisThis()
# pg1.canRun()
# pg1.whatType()
# pg1.canSwim()
#
# # Data Encapsulation
# class personalComputer:
#     def __init__(self):
#         self.maxComputerPrice = 20000
#
#     def mySell(self):
#         print("Selling price : {}".format(self.maxComputerPrice))
#     def setMaxComputerPrice(self , price):
#         self.maxComputerPrice = price
#
# pc = personalComputer()
# pc.mySell()
#
# # change the price
# pc.maxComputerPrice = 40000
# pc.mySell()
#
# # or using set function
# pc.setMaxComputerPrice(60000)
# pc.mySell()

# print('------------------------------------Nested Dictionary---------------------------')
# people = {
#     1 : {'Name':'Simran' , 'age':'20','sex':'F'},
#     2 : {'Name':'simmu' , 'age' : '19','sex':'F'}
# }
# print(people)
# print(people[1]['Name'])
# print(people[2]['Name'])
# print(people[1]['sex'])
# '''addind elements to dict'''
# people[3] = {}
# people[3]['Name'] = 'Luna'
# people[3]['age'] = '30'
# # people[3]['sex'] = 'M'
# '''Iteration'''
# print(people.items())
# for p_id , p_info in people.items():
#     print("\nPeople id:", p_id)
#     for key in p_info:
#         print(key +':' + p_info[key])
#
# print(26//3)
#

# print("------------------------------Overloading Operator----------------- ")
# class myPoint:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return '({0},{1})'.format(self.x,self.y)
#
#     def __add__(self, other):
#         s1 = self.x + other.x
#         s2 = self.y + other.y
#         s3 = myPoint(s1 ,s2)
#         return s3
#
#     def __sub__(self, other):
#         sb1 = self.x - other.x
#         sb2 = self.y - other.y
#         sb3 = myPoint(sb1 , sb2)
#         return sb3
#
#
#     def __lt__(self, other):
#         s1 = self.x + self.y
#         s2 = other.x + other.y
#         return s1 < s2
#     def __gt__(self, other):
#         mag1 = self.x**2 + self.y**2
#         mag2 = other.x*22 + other.y**2
#         return mag1 > mag2
# p1 = myPoint(1,2)
# p2 = myPoint(2,5)
# p3 = p1 + p2
# print(p1)
# print(p2)
# print()
# print(p1>p2)
# print(p1.__lt__(p2))
# print(p1 <p2)
# print()
# print(p1.__gt__(p2))
# print(p2.__gt__(p1))
# print(p1+p2)
# print()
# print(p1-p2)
#


# print("---------------------Polymorphism---------------------------")
# '''1. Duck typing'''
# class pyCharm:
#     def execute(self):
#         print("Compiling")
#         print("Running")
#
# class MyEditor:
#     def execute(self):
#         print("spell check")
#         print('Convention check ')
#         print('Compiling')
#         print('Running')
# class laptop:
#      def code(self, ide):
#      ide.execute()

# print('----------------------------------Method Overloading---------------------')
# class Student:
#     def __init__(self,m1 , m2):
#         self.m1 = m1
#         self.m2 = m2
# #     def sum(self,a=0,b=0,c=0):
# #         s = a+b+c
# #         return s
# # s1 = Student(2,3)
# # print(s1.sum(a=1,c=5))
# # print(s1.sum(1,2))
# #     Or
#     def sum(self,a = None,b = None,c=None):
#         s =0
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#             return s
#         elif a!= None and b!=None:
#             s = a+b
#             return s
#         else:
#             s=a
#             return s
#
# s = Student(25,67)
# print(s.sum(11,5654))
#
# print('------------------------------------Method Overridding----------------------')
# class A:
#     def show(self):
#         print("In A show")
#
# class B(A):
#     # pass
#     def show(self):
#         print("In B show")
# # a = A()
# # a.show()
# # BUTTTTTTTT if
# a = B()             #we have to inherited
# a.show()            #Now this show works
#
# # but what if we have show inside of B also...lets look
# '''We got show of B not of A ...........That's what Overridding is '''


# print('----------------------------Generators---------------------------')
# def TopTen():
#     # return 5
#     yield 5
#     yield 4
#     yield 3
#     yield 2
#     yield 1
# values = TopTen()
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
#
# # ----------------------Reverse string------------
# print("-=---------------------------reverse String-------------------")
#
#
# def reversestr(my_string):
#     l = len(my_string)
#     for i in range(l-1,-1,-1):
#         yield my_string[i]
# r = reversestr("hello")
# for char in r:
#     print(char)
#
# print("----------------------Square upto top ten-------------------")
#
#
# def topTen():
#     n= 1
#     while n <= 10:
#         sq = n**2
#         yield sq
#         n += 1
# values = topTen()
# for i in values:
#     print(i)
#
# print('--------------------------------Decorators-------------------')
# def div(a,b):
# #     print(a/b)
# # div(15 , 3)                   #It working but what if the deno is greater than num
# # div(2,4)                      #its also working but i want to swap them
#     if a > b:
#         print(a/b)
#     else:
#         # temp = a
#         # a  = b
#         # b = temp              OR
#         a,b = b,a
#         print(a/b)
# div(2,4)
#
# def div(a,b):
#     print(a/b)
#
# def smart_div(fun):
#     def inner_fun(a,b):
#         if a < b:
#             a,b = b,a
#         return fun(a,b)
#     return inner_fun
# div1 = smart_div(div)
# div1(2,4)
#
# def make_decorated(fun):
#     def inner_fun():
#         print('I got decorated')
#         fun()
#     return inner_fun
# def simple_func():
#     print("I am a simple function")
# decor = make_decorated(simple_func)
# decor()
#
#
# def Name():
#     print('My name is Simran!')
# # Now I want to add my age in this function
# def Age(fun1):
#     def inner_func():
#         print("My age is 20 years .")
#         fun1()
#     return inner_func
# myAge = Age(Name)
# myAge()
#
#
# print("-------------------------------while loop-------------------------")
# i=1
# while i < 10:
#     print(i)
#     i+=1
# else:
#     print("Numbers printed successfully!")

# print("-----------------------------------Patterns--------------------")
# print('    *')
# print('   ***')
# print("  *****")
# print(' *******')
#
# print()
# for i in range(1,5,1):
#     print('#',end='/')
#
# print()
# print("--------------Sqaure Pattern---------")
# for j in range(5):
#     for i in range(5):
#         print('&',end=' ')
#     print()
# for j in range(5):
#     print("&",end=' ')
# print()
#
# print('-----------Triangular Pattern-----------')
# for i in range(4):
#     for i in range(i):
#         print('*',end = ' ')
#     print()
#
# print()
#
# for i in range(4):
#     for i in range(3-i):
#         print('#',end=' ')
#     print()

# print('Take input from user..........')
# n: int = int(input("Enter the value of n : "))
#
# for i in range(n):
#     for j in range((n-i)):
#         print(j+1, end=' ')
#     print()

# for i in range(n):
#     for j in range((n-i)):
#         print(i+j+1, end=' ')
#     print()

# # outer loop
# for i in range (65,70):
#     # inner loop
#     for j in range(65,i+1):
#         print(chr(j),end="")
#     print()
#
#
# for i in range (65,69):
#     # inner loop
#     for j in range(81,84):
#         print(chr(j),end=" ")
#     print()

# n = int(input("Enter the value of n : "))
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(' ',end= ' ')
#     for j in range(1,2*i):
#         print('*',end=' ')
#     print()
#
#
# n = int(input("Enter the value of n : "))
# for i in range(n,0,-1):
#     for space in range(n-i):
#         print(' ',end= ' ')
#     for j in range(1,2*i):
#         print('*',end=' ')
#     print()

# n = int(input("Enter the value of N : "))
# m = int((n+1)/2)
# print(m)
# for i in range(1,n+1):
#     if i <= m:
#         s = i-1
#         b = 2*(m-i)+1
#     else:
#         s = n-i
#         b = 2*(i-m)+1
#     for space in range(s):
#         print(' ', end=' ')
#     for j in range(b):
#         print("*", end=' ')
#     print()

# n = int(input("Enter the value of n : "))
# m = int((n+1)/2)
# for i in range(1,n+1):
#     if i <= m:
#         s = m-i
#         b = 2*i-1
#     else:
#         s = i-m
#         b = 2*(n-i)+1
#     for space in range(s):
#         print(' ',end=' ')
#     for j in range(b):
#         print('*',end=' ')
#     print()

# print("---------------------------------Matrix---------------------------")
# a = [
#     ['A',1,2,3,5,5],
#     ['B',5,6,7,8,8]
# ]
# print(a)

# n = 2
# m = 3
# a = [0]*m
# print(a)
# for i in range(m):
#     a[i] = [0]*n
# print(a)

# a = 60
# b = 25
# r1 = a
# r2 = b
# while(r2>0):
#     q = r1/r2
#     r = (r1-q)*r2
#     r1 = r2
#     r2 = r
# print(r)
# t = int(input().strip())
# for i in range(1,t+1):
#     n = int(input().strip())
#     sum = 0
#     for j in range(1,n):
#         if j%3 == 0 or j%5 == 0:
#             # print(j)
#             sum = sum + j
#     print(sum)

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     count = 1
#     sum =0
#     fibo1 = 1
#     fibo2 = 1
#     while (count <= n):
#         # print(fibo1)
#         sum = fibo1 + fibo2
#         fibo2 = fibo1
#         fibo1 = sum
#         count += 1
#         # print(sum)
# result = 0
# for i in range(fibo1):
#     if i%2 == 0:
#         result = result + i
# print(result)

# import numpy as np
# np.ones([1,2,3,4])
# print(ones)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# list2 = []
# for i in arr:
#     if i not in list2:
#         list2.append(i)
# print(list2[-2])


# for _ in range(int(input())):
#     name = input()
#     score = list(float, input())
#     # score.sort()
# print(score)


# if __name__ == '__main__':
#     N = int(input())
#     list = []
#     str = input()
#     for i in range(N):
#         if str == "insert":
#             i, e = list.insert(i, e)

#         if str == 'print':
#             print(list)

#         if str == 'remove':
#             list.remove(e)

#         if str == "sort":
#             list.sort()

#     print(list)

# n = int(input())
# s = set(map(int, input().split(" ")))
# m = int(input())
# for i in range(0,m):
#     x=list(input().split(" "))
#     if x[0]=="pop":
#         s.pop()
#     elif x[0]=="remove":
#         j = int(x[1])
#         s.remove(j)
#     elif x[0]=="discard":
#         j = int(x[1])
#         s.discard(j)
# print(sum(s))

n1 = int(input())
A = set(map(int,input().split()))
n2 = int(input())
B = set(map(int,input().split()))
# c = set(A.union(B))
# print(c)
# count =0
# for i in c:
#     count+=1
# # print(str(count))
# print(count)
c = set(A.union(B))
print(len(c))