n=int(input())
k=[]
for i in range(2,n+1):
    for j in range(2,n+1):
        if i*j==n:
            k.append(i)
            k.append(j)
            break
l=list(set(k))
l.sort()
if k==[]:
    print(-1)
else:
    print(*l)