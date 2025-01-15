t=int(input())
for k in range(0,t):
    x,y=map(int,input().split())
    if x<=y:
        print('0')
    elif x%y==0:
        print(y)
    else :
        print(x%y)
        