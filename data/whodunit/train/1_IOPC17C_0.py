for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    min=0
    for i in a:
        if ((i%m) >min) :
            min = i%m 
    print(min)
    i=i+1
