t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    if(sum(a)%2==1):
        print("YES")
    else:
        print("NO")