'''Write a program to take user choice for print the number either
in horizontal or vertical and from 7 to 100 with updation of 2. '''


choice = input("For horizontal type(h),for vertical type(v) : ")

if(choice=='h'):
    for i in range(7,101,2):
        print(i,end=" ")

elif(choice=='v'):
    for i in range(7,101,2):
        print(i)

else:
    print("invalid value",choice)
 
