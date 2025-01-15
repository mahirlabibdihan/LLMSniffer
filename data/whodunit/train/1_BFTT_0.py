t=int(input())
while t>0:
    n=int(input())
    k=str(n+1)
    while k.count("3")<3:
        k=int(k)
        k+=1
        k=str(k)
    print(k)
    t-=1
