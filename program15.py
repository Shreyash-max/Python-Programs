# Write a program to find factorial of a number.

n=int(input("Enter any number : "))
fact=1
for i in range(1,n+1,1):
    fact*=i

print("factorial is = ",fact)    
