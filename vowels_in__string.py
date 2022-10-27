s=input()
l=['a','e','i','o','u','A','E','I','O','U']
l1=[]
for i in s:
    if i in l:
        if i not in l1:
            l1.append(i)
for i in l1:
    print(i,end=' ')
