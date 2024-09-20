# Write a program to check number is divisible 3 or 7 or both ? 

print("To check number is divisible by 7 and 3 or not")

a = int(input("Enter any number : "))

if((a%3==0) and (a%7==0)):
    print(a, "is divisible by 3 and 7 both")

elif(a%3==0):
    print(a, "is divisible by 3 only")

elif(a%7==0):
    print(a, "is divisible by 7 only")

else:
    print("Not divisible")
