try:
    for _ in range(int(input())):
        N = int(input())
        for __ in range(N):
            a, b = map(int, input().split())
            
        ans = 1
        for i in range(2, N + 1):
            ans ^= i
            
        print(ans)
    
except Exception as e:
    print(e.__class__)