s=input()
l=["a","e","i","o","u","A","E","I","O","U"]
l1=[]
c=0
for i in s:
    if i in l:
        c+=1
print(c)