#Write the code using function to find area and perimater of rectangle
def p(a,b):
    peri=2*(a+b)
    return peri
def c(a,b):
    area=a*b
    return area
a = int(input("Enter lenght : "))
b = int(input("Enter Breadth : "))
print(p(a,b))
print(c(a,b))