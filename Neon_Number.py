n=int(input())
sum=0
k=n*n
while k>0:
    r=k%10
    sum+=r
    k=k//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")