s=int(input())
e=int(input())
def selfd(n):
    if n<10:
        return True
    num=n
    while n>0:
        r=n%10
        if r==0:
            return False
        if num%r!=0:
            return False
        n=n//10
    return True
for i in range(s,e+1):
    if selfd(i):
        print(i,end=" ")
    
    