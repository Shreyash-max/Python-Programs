#Write a function to reverse a string and take s string as user input

def x(s,s1):
    for i in s:
        s1 = i+s1
    return(s1)
s = str(input(": "))
s1 = ""
print(x(s,s1))    