n=int(input())
l=list(map(int,input().split()))
m=[]
r=[]
for i in l:
    if i%2==0:
        m.append(i)
    if i%2 != 0:
        r.append(i)
q=m+r
print(*q)
    
        
   