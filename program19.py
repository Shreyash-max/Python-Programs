# Write a program to find fibonacci series.

n = int(input("Enter any number : "))
a=0
b=1
s=1
for i in range(1,n+1,1):
    print(a,end=" ")
    s=a+b
    b=a
    a=s
