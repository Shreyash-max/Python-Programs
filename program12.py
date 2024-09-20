# Write a program to check number is greater among three number by using nested if ?

a = int(input("Enter any number a : "))
b = int(input("Enter any number b : "))
c = int(input("Enter any number c : "))

if(a>b):
    if(a>c):
        print(a,"is greater")

    else:
        print(c,"is greater")

else:
    if(b>c):
        if(b>a):
            print(b,"is greater")

        else:
            print(c,"is greater")
