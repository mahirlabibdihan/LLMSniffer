t=int(input())
for i in range(t):
    n=int(input())
    l=[int(j) for j in input().split()][:n]
    if sum(l)%2==0:
        print("NO")
    else:
        print("YES")