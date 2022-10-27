s=input()
l=s.split(" ")
l1=[]
for i in range(len(l)):
    k=l[i]
    k1=k[::-1]
    l1.append(k1)
l1.reverse()
j=" ".join(l1)
print(j)
