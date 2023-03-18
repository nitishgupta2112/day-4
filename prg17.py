n = int(input())
while n>0:
    b=str(n+1)
    if b == b[::-1]:
        print(b)
        break
    else:
        n = n+1