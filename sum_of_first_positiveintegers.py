#Sum of the First n Positive Integers

#Write a program that reads a positive integer, n, 
#from the user and then displays the sum of all of the integers from 1 to n. 
#The sum of the first n positive integers can be computed using the formula:
#sum = (n)(n + 1) / 2

#Get the number
n=int(input('Enter the number: '))
#Find the Sum 
sum=(n*(n+1))/2
#Print the output.
print('The sum of first %d positive integers is %d' %(n,sum))
