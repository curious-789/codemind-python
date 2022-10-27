m=int(input())
l=list(map(int,input().split()))
z=l[:m//2]
zz=l[m//2:]
k=[]
for i in range(len(z)):
    k.append(z[i])
    k.append(zz[i])
print(*k)