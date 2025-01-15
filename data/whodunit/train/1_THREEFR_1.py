t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(x+y+z==(2*max(x,y,z))):
        print("yes")
    else:
        print("no")