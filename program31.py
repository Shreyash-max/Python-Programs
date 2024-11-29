p = int(input("Enter prize : "))
n = int(input("Enter quantity : "))
a = p*n
if(10000 > a > 999):
    c = a*15//100
    d = a+c 
    print(a ,c ,d)
elif(a<1000):
    c = a*10//100
    d = a+c
    print(a ,c ,d)   
elif(a > 9999):
    e = a*20//100
    r = e+a
    c = r*2//100
    d = e+c
    j = a+e+c
    print(a ,d ,j)     



