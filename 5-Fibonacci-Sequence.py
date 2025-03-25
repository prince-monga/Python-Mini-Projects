#Fibonacci Sequence
'''
The Fibonacci Sequence is a series of numbers where each number is the sum of the previous two numbers.
ex. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''
# Input from user 
n=int(input("Enter Number of terms: "))

#intialitze First two term---
a,b=0,1
if n<=0:
    for i in range(n):
        print(a,end=" ")
        nth=a-b
        a=b
        b=nth    
elif n==1:
    print(" ",a," ")    
else:
    for i in range(n):
        print(a,end=" ")
        nth=a+b
        a=b
        b=nth
