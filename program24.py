#Write a code using a function to check person is eligible to vote
def x(a):
    if(a>=18):
        return("Eligible to vote")
    if(a<=17):
        return("Not Eligible")
    else:
        return("Entry is Invalid")
a=int(input("Enter your age : "))
print(x(a))   