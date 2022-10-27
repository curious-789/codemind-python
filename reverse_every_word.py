n=input()
l=n.split()
l1=[]
for i in range(len(l)):
    s=l[i][::-1]
    l1.append(s)
print(*l1)