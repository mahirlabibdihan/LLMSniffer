for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=max(l)
    if c>=b:
        print("YES")
    else:
        print("NO")
