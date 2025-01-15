n = int(input())
arr = list(map(int, input().split()))

ans = sum(arr)

if(ans == (n*(n+1)) / 2):
    print("YES", end = "")
else:
    print("NO", end = "")