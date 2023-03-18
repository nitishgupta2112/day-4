str1 = input()
str2 = input()
str3=""
for i in str1:
    for j in str2:
        if(i==j and i!=" "):
            str3=str3+i
print(*(set(str3)),sep="")


