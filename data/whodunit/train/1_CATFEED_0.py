for _ in range(int(input())):
    n,m=map(int, input().split())
    l=list(map(int, input().split()));h=[]
    for i in range(n):
        h.append(0)
    h[l[0]-1]=1
    for i in range(1,m):
        h[l[i] - 1] += 1
        if h[l[i]-1]==min(h)+2:
            print("NO")
            break

    else:
        print('YES')
