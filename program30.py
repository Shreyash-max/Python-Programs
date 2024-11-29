#Write a program to take a integer from user and print the sum of all natural numbers
n = int(input())
s = 0
for i in range(1,n+1):
    s += i
    print(s)