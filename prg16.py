def prime(i):
    for k in range(2,i):
        if k%i==0:
            return False
    return True
def fun(a):
    for i in range(a,1,-1):
        if a%i==0 and prime(i):
            return i
a = int(input())
b = 0