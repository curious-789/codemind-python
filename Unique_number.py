x=int(input())
l=[]
while x>0:
    rem=x%10
    l.append(rem)
    x=x//10
for i in l:
    if l.count(i)>1:
        print("Not Unique Number")
        break
else:
         print("Unique Number")
