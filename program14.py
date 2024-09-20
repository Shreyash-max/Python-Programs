# Write a program to count numbers of even and odd from (1 to 20).

even=odd=0
for i in range(1,21,1):
    if(i%2==0):
        even+=1

    else:
        odd+=1

print("even=",even)
print("odd=",odd)
