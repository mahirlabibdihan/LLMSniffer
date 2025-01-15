def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [int(input()) for _ in range(Q)]
    
    count = [0]*1000001
    min_val = A[0]
    start = 0
    for i in range(N):
        if A[i] != min_val:
            count[min_val] += ((i-start)*(i-start+1))//2
            start = i
            min_val = A[i]
    count[min_val] += ((N-start)*(N-start+1))//2
    
    for i in range(1000000, 0, -1):
        count[i-1] += count[i]
    
    for k in queries:
        print(count[k])

solve()