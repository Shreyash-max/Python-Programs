# Write a program to find the words of a numbers

n=int(input("Enter a  number : "))
while(n!=0):
    r=n%10
    print(r,end="")
    n=n//10
