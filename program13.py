# Write a program to multiply the even numbers and odd numbers from 1 to 20.

even=odd=0
for i in range(1,21,1):
    if(i%2==0):
        even*=i

    else:
        odd*=i

print("enen=",even)
print("odd=",odd)
