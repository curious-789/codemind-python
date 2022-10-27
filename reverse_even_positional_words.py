n=input()
l=n.split()
l1=[]
for i in range(len(l)):
    if i%2==0:
        s=l[i][::-1]
        l1.append(s)
    else:
        l1.append(l[i])
print(*l1)