for _ in range(int(input())):
    a,b,c,d=[int(x) for x in input().split()]
    if a==b:
        print("YES")
    elif c==d:
        print("NO")
    elif abs(a-b)%abs(c-d)==0:
        print("YES")
    else:
        print("NO")