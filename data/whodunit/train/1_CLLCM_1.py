for t in range(int(input())) :
    n=int(input())
    a=list(map(int,input().split()))
    itn=0
    for i in a:
        if i%2==0:
            itn=2
            print("NO")
            break
    if itn==0:
        print("YES")