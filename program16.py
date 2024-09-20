# Write a program to print the numbers in several order according to user input till 1 by using while loop.


j = int(input("Enter any number : "))

i=1
while(i<j+1):
    print(j,end=" ")
    j-=1
