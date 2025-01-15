t=int(input())
while(t>0):
    x,y,k=map(int,input().split())

    add=x+y
    if(add%(2*k)<k):
        print("Chef")
    else:
        print("Paja")
    t-=1


