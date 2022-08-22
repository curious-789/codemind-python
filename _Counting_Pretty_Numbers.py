t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    cnt = 0
    for j in range(l,r+1,+1):
        if(j%10 == 2 or j%10 == 3 or j%10 == 9):
            cnt+=1
    print(cnt)