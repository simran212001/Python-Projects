"""def listSum(numbers):
    if not numbers:
        return 0

    else:
        (f,rest)=numbers
        return f+listSum(rest)
myList=(1,(2,(3,None)))
total =listSum(myList)"""

def point_distance(x_0, y_0, x_1, y_1):
    """ Return distance between two points (x0,y0) and (x1,y1) """
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1
    return (x_dist ** 2 + y_dist ** 2) ** 0.5

# Compute distance between (2, 2) and (5, 6). Should be 5.0
x_0, y_0 = 2, 2
x_1, y_1 = 5, 6
print(point_distance(x_0, y_0, x_1, y_1))


"""def welcome():
    answer="welcome to location " 
    return answer
print(welcome())

#or
def welcome(location):
    answer="welcome to "+location
    return answer
print(welcome("the matrix"))


def welcome(location):
    answer="welcome to "+location
    print(answer)
    print("simran")
welcome("python scripting")
"""

def welcome(location):
    answer="welcome to "+location
    print(answer)
    
print(welcome("python scripting"))

def tricky():
    return
print(tricky())

def miles_to_feet(miles):
    return miles*5280
miles=13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


def total_seconds(hours,minutes, seconds):
    return hours*3600+minutes*60+seconds



###################################################
# Tests
# Student should not change this code.

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")
def rectangle_area(width ,height):
    return width*height
width,height=4, 3
print("A rectangle"+ str(width) +"inches wide and"+str(height)+
      "inches high has an area of "+str(rectangle_area(width,height)))


"""
Template - Compute the circumference of a circle, given the length of its radius.
"""
import math
PI=math.pi

def circle_circumference(radius):
    return 3.141*(radius)**2
radius=3
print("a circle of radius" + str(radius) +"has area equals to"+str(circle_circumference(radius)))


