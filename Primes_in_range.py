from math import *
def is_prime(n):
    if (n==1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def get(n,m):
    a=0
    for i in range(n,m+1):
        if is_prime(i):
            a+=1
    return a
n=int(input())
m=int(input())
print(get(n,m))