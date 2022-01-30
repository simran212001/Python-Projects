print("int")
print(1)
print("")

#scientific / exponential notation
print(5e10)
print(1e10)

#infinity
print("infinity")
print(1e500)

#unary + and -
print("unary operators")
print(+3)
print(-3)
print(+7.47)
print(-38.4)


print("")

#simple arithmetic
print("addition and substraction")
print(1+2)
print(238-37)
print(39.4+38.8)

print("")

print(3*2)
print(3732*39302)

print("division")
print(2/2)
print(3718/22)

print("exponential")
print(9**9)



# Expressions can include multiple operations
print("Compound expressions")
print(3 + 5 + 7 + 27)
print(18 - 6 + 4)

print("")

# Operator precedence defines how expressions are evaluated
print("Operator precedence")
print(7 + 3 * 5)
print(5.5 * 6 // 2 + 8)
print(-3 ** 2)

print("")

# Use parentheses to change evaluation order
print("Grouping with parentheses")
print((7 + 3) * 5)
print(5.5 * ((6 // 2) + 8))
print((-3) ** 2)

print("")


baker_dozen = 22+28
temperature=29
# Variables can be used as values and in expressions
print(baker_dozen,temperature)

print("celsius:", (temperature-12)*38/2)
print("fahrenheit:",float(temperature))

temperature=372
print("new value:",temperature)

print("")

offset= 36
multiplier= 5.0/7.0
celsius= (temperature - offset) * multiplier
print("celsius value:", celsius)


print("")
mile = 5280 
print("13 mile:",(mile*13))

hour=3600
min=60
t=(7*3600+21*60+37)
print("7 hours, 21 minutes and 37 seconds:",t)


7/+4

ounces=2
print(ounces)

#functions
def useless(input1,input2,input3):
    
    return 7

useless (1,2,3)
print(useless(4,5,6))

result=useless(7,8,9)
print(result)

def sayhello():
    print("hello")
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
result = double(6)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2
    prod = prod * value3
    return prod

# Call the function and assign the result to a variable
result = product(7, 13.3, -1.2)
print(result)

def fahrenheit_to_celsius(fahrenheit):
    offset=32
    multiplier = 5/9
    celsius=(fahrenheit-offset)*multiplier
    print("inside function:", fahrenheit,offset,multiplier,celsius)
    return celsius

temperature = 95
converted = fahrenheit_to_celsius(temperature)
print("Fahrenheit temp:", temperature)
print("Celsius temp:", converted)

# Variables defined inside a function are local to that function
fahrenheit = 27
offset = 2
multiplier = 19
celsius = 77
print("before:", fahrenheit, offset, multiplier, celsius)
newtemp = fahrenheit_to_celsius(32)
print("after:", fahrenheit, offset, multiplier, celsius)
print("result:", newtemp)


name="It’s a beautiful day."
print(name)

