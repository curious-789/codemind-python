t,s,b=map(int,input().split())
c=2*s*t*b*512
tc=c//1024
print('{}KB'.format(tc))