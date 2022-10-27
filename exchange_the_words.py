s=input()
l=s.split(" ")
l1=[]
for i in range(len(l)):
    k=l[i]
    l1.append(k)
l1.reverse()
j=" ".join(l1)
print(j)