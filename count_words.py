s=input()
s1=s.split(" ")
l=["a","e","i","o","u","A","E","I","O","U"]
l1=[]
c=0
for i in s1:
    if i[0] in l and i[len(i)-1] not in l:
        
        c+=1
print(c)