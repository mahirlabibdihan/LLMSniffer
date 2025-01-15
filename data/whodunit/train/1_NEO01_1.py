for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split())) 
    A = sorted(A)[::-1]
    left = 0
    summ = sum(A)
    right = summ
    ans = -float('inf')
    for i in range(n):
        left += A[i]
        right -= A[i]
        ans = max(ans, (i+1)*left + right)
    print(ans)