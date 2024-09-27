# Write a program to find the number of vowel and consonent in given string

S = "Hello Class"

Vowel = "aeiouAEIOU"
V=C=0
for i in S:
    if i in (Vowel):
        V+=1

    else:
        C+=1

print("Vowel=",V)
print("Conconent=",C)
