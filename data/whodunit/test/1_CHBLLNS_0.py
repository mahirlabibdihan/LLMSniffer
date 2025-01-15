t = int(input())
for _ in range(t):
    r, g , b = map(int, input().split())
    k = int(input())
    
    print(min(k-1, r) + min(k-1, g) + min(k-1, b) + 1) 