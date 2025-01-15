t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a==b:
        print("YES")
    elif a!=b and c==d:
        print("NO")
    else:
        if abs(a-b)%abs(c-d)==0:
            print("YES")
        else:
            print("NO")