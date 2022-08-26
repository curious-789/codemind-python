t=int(input())
for i in range(t):
    l=input()
    s=l.split(" ")
    n=int(s[0])
    a=int(s[1])
    b=int(s[2])
    k=int(s[3])
    q=(n/a)+(n/b)
    if(q>k):
        print('Win')
    else:
        print('Lose')
