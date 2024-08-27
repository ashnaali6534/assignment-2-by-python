# Question-number-1
# program that calculates age

print("Age Calculator")
def ageCalculator():
    current_year:int= int(input("Enter the current year:"))
    birth_year:int = int(input("Enter your birth year: "))
    age:int=current_year-birth_year
    return age
output = ageCalculator()
print("Your age is:", output ,"years")

#/****************************************************************

# Question-number-2
# program that calculates the area of rectangle
print("rectangular area calculator")
def calculateArea():
    length:float = float(input("Enter the length: "))
    width:float = float(input("Enter the width: "))
    area:float = length * width
    return area
outputofarea = calculateArea()
print("The area of the rectangle is:", outputofarea ,"metersquared")

# /****************************************************************

# Question-number-3
# program that calculates the area of circle
print("circle Area Calculator")
def calculateAreaofCircle():
    radius:float = float(input("Enter the radius of the circle : "))
    area:float = 3.14 * radius * radius
    return area
outputofarea = calculateAreaofCircle()
print("The area of the Circle is : " , outputofarea ,"metersquared")

# /****************************************************************

# Question-number-4
# program that calculates the area of cube

print("cube area calculator")
def calculateAreaofCube():
    side:float = float(input("Enter the side of the cube: "))
    area:float = side * side * side
    return area
outputOfCube = calculateAreaofCube()
print("The area of the Cube is : " , outputOfCube , "metercube")

# /****************************************************************

# Question-number-5
# program that calculates the volume of cylinder
print("volumeOfCylinderCalculator")
def calculateVolumeOfCylinder():
    radius:float = float(input("Enter the radius of the cylinder: "))
    height:float = float(input("Enter the height of the cylinder: "))
    volume:float = 3.14 * radius * radius * height
    return volume
outputOfCylinder = calculateVolumeOfCylinder()
print("The volume of the Cylinder is : " , outputOfCylinder , "metercube")

# # /****************************************************************

# # Question-number-6
# # program that calculates the percentage
print("PercentageCalculator")
def calculatePercentage():
    totalNumber:float = float(input("Enter the  total numbers: "))
    obtainedNumber:float = float(input("Enter the  obtained numbers: "))
    percentage:float = (obtainedNumber / totalNumber) * 100
    return percentage
outputOfPercentage = calculatePercentage()
print("The percentage is : " , outputOfPercentage ,"%")

# # /****************************************************************

# Question-number-7
# program that converts temperature from celcius to fahrenheit
print("temperature convertor program")
def convertTemperature():
    temperature:float = float(input("Enter the temperature in Celsius: "))
    result:float = (temperature * 9/5) + 32
    return result
outputOfTemperature = convertTemperature()
print("The temperature in Fahrenheit is: ", outputOfTemperature , " degrees")

# /****************************************************************

# Question-number-8
# program that converts temperature from fahrenheit to Celsius
print("temperature convertor program")
def convertTemperatureToCelsius():
    temperature:float = float(input("Enter the temperature in Fahrenheit: "))
    result:float = (temperature - 32) * 5/9
    return result
outputOfTemperatureToCelsius = convertTemperatureToCelsius()
print ("the temperatue in celsius is : ",outputOfTemperatureToCelsius ," degrees")

# /****************************************************************

# Question-number-9
# program that converts minutes into seconds
print("time convertor program")
def convertMinutesToSeconds():
    minutes:float = float(input("Enter the minutes: "))
    seconds:float = minutes * 60
    return seconds
outputOfMinutesToSeconds = convertMinutesToSeconds()
print("The time in seconds is: ", outputOfMinutesToSeconds , " seconds")

# /****************************************************************

# Question-number-10
# program that calculates BMI
print("BMI calculator program")
def calculateBMI():
    weight:float = float(input("Enter your weight in kg: "))
    height:float = float(input("Enter your height in meters: "))
    bmi:float = weight / (height * height)
    return bmi
outputOfBMI = calculateBMI()
print("Your BMI is: ", outputOfBMI)

# /****************************************************************
