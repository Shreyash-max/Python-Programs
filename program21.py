def x(a,b):
    if(a>77):
        return("Eligile")
    elif(a>50 and b>90):
        return("Eligible")
    else:
        return("Not Eligible")
a=int(input("Enter Attendance : "))
b=int(input("Enter Marks : "))
print(x(a,b))