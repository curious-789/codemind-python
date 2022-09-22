n=int(input())
for i in range(n):
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
if (n==1):print('Ugly Number')
else:print('Not Ugly Number')