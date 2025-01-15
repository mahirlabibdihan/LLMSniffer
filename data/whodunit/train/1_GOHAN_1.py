t=int(input())
while(t):
    t-=1
    r,l,c,v=list(map(int,input().split()))
    print(1-c*r*r/(4*l))