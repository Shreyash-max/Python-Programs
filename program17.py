# Write a program to count numbers of digit.

n = int(input("Enter a number : "))
count=0
while(n!=0):
    r=n%10
    count+=1
    n=n//10

print(count)    
