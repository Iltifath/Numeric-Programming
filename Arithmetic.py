#Arithmetic

#Create a program that reads two integers, a and b, from the user. Your program should compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of ab

#Import math library
import math

#Get two integers
a=int(input('Enter two integers\na:'))
b=int(input('b:'))
#Addition
print("Sum of two integers:",a+b)
#Subtraction
print("Difference of two integers:",a-b)
#Multiplication
print("Multiplication of two inetgers",a*b)
#Quotient
print("Quotient of two integers:",a//b)
#Reminder
print("Reminder of two integers:",a%b)
#Lograthmoc
print("Log of first integer:",math.log10(a))
#Result ab
print("Result of ab:",a*b)
