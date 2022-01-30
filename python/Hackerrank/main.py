# if __name__ == '__main__':
#     N = int(input())
#     L=[];
#     for i in range(0,N):
#         cmd=input().split();
#         if cmd[0] == "insert":
#             L.insert(int(cmd[1]),int(cmd[2]))
#         elif cmd[0] == "append":
#             L.append(int(cmd[1]))
#         elif cmd[0] == "pop":
#             L.pop();
#         elif cmd[0] == "print":
#             print(L)
#         elif cmd[0] == "remove":
#             L.remove(int(cmd[1]))
#         elif cmd[0] == "sort":
#             L.sort();
#         else:
#             L.reverse();

#
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     t = tuple(integer_list)
#     print(hash(t))


# def swap_case(s):
#     return s.swapcase()
#
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
# import textwrap
#
# def wrap(string, max_width):
#     return textwrap.TextWrapper(width=max_width).fill(string)
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# def average(array):
#     return (sum(set(array)) / len(set(array)))
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# n1 = int(input())
# A = set(map(int,input().split()))
# N = int(input())
# for i in range(N):
#     X = list(input().split(" "))
#     if X[0] == "update":
#         y = set(map(int,input().split()))
#         A.update(y)
    
#     if X[0] == "intersection_update":
#         y = set(map(int,input().split()))
#         A.intersection_update(y)
    
#     if X[0] == "symmetric_difference_update":
#         y = set(map(int,input().split()))
#         A.symmetric_difference_update(y)

#     if X[0] == "difference_update":
#         y = set(map(int,input().split()))
#         A.difference_update(y)
    
# print(sum(A))   



# import math
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(pow(a,b)+ pow(c,d))

# a = int(input())
# b = int(input())
# print(a//b)
# print(a%b)
# print(divmod(a,b))


# import cmath
# z = complex(input())
# print(abs(z))
# print(cmath.phase(z))

# from itertools import product
# A =list(map(int,input().split()))
# B = list(map(int,input().split()))
# print(*product(A,B))

# from itertools import permutations
# A = input().split()
# S = A[0] 
# k = int(A[1])
# Ans = list(permutations(S,k))
# # print(sorted(Ans))         not acceptable
# for i in sorted(Ans):
#     print(''.join(i))

# from collections import Counter


# X = int(input())
# Size = Counter(map(int,input().split()))
# N = int(input())
# Cost = 0
# for i in range(N):
#     Xi = input().split()
#     CustSize = int(Xi[0])
#     Price = int(Xi[1])
#     if Size[CustSize]:
#         Cost = Cost + Price
#         Size[CustSize] -= 1
# # print(X)
# # print(Size)
# # print(N)
# # print(Xi)
# # print(CustSize)
# # print(Price)
# print(Cost)


# from collections import namedtuple

# No_of_students = int(input())               
# Student = namedtuple('Student' , 'ID Name Class Marks')    
# total_marks = 0        
# for i in range(No_of_students):
#     ID = int(input())  
#     Name = str(input()) 
#     Class = int(input()) 
#     Marks=int(input()) 
#     St = Student(ID, Name, Class, Marks)
#     total_marks = total_marks + St.Marks
# print(total_marks/No_of_students)


# import calendar

# day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

# d ,m,y = map(int,input().split())
# print(day[calendar.weekday(y,m,d)])


# import math
# import os
# import random
# import re
# import sys
# from datetime import datetime

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
#     return str(int(abs((t1-t2).total_seconds())))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()


# N , X = map(int,input().split())
# Sublist = list()
# for _ in range(X):
#     Sub = map(int,input().split())
#     Sublist.append(Sub)
# print(Sublist)
# for i in zip(*Sublist):
#     print(i)
#     print(sum(i))
#     print(len(i))
#     print(sum(i)/len(i))


from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y :x*y , fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(map(int, input().split())))
    result = product(fracs)
    print(result)