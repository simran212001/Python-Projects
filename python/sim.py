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
print('----------------new aray with the same elemnts------------------')
newArr = array(vals.typecode , (a for a in vals))
for e in newArr:
    print(e)
print('---------------Square of the elements of newArr ----------------')
newArr = array(vals.typecode , (a*a for a in vals))
print(newArr)
for e in newArr:
    print(e)

print('---------------ask a user to enter the valus in an empty array----------')
from array import *
arr = array('i',[])
n = int(input('Enter the length of the array'))
for i in range(n):
    x = int(input('Enter the element:'))
    arr.append(x)
print(arr)

print('----------------Search an element-------------')
s = int(input('Enter the value you want to seach:'))
for i in range(len(arr)):
    if s == arr[i]:
        print("The index number for this value is:",i)
print("---------or--------")
k=0 #index number
for e in arr:
    if e == s:
        print(k)
        break
    k+=1

print('-----Seach with functions----------')
print(arr.index(s))

# from numpy import *
# ar = array([1,2,3],[1,2,3])
# print(ar)