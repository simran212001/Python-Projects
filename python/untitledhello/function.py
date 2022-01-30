def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2
      

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))


def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())



def f(x):
    return -5*(x)**2+67*(x)**2-47
print(f(0))
print(f(1))
print(f(2))


#boolean
value1=True
value2=False
print(value1,value2)
print("")

# Logical NOT
print("Logical NOT")
print("===========")
print(not value1)
print(not value2)

print("")

# Logical AND
print("Logical AND")
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

print("")

# Logical OR
print("Logical OR")
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)

print("")

value3 = True
value4 = True

print(value2 or ((value1 and value4) or value3))



'''print("conditional")
def greet(friend,money):
    if friend:
        print("hi")
    if money>20:
        money=money-20
    return money
money=25

money=greet(False,money)
print("Money:",money)
print()

money=greet(True,money)
print("Money:",money)
print()

money=greet(True,money)
print("Money:",money)
print()
'''

def greet(friend,money):
    if friend and (money>20):
        print("hi")
        money=money-20
    elif friend:
        print("hello")
    else:
        print("Ha Ha")
        money=money+10
    return money

money=15
money=greet(False,money)
print("Money:",money)
        




















            
