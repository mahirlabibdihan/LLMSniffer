T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd = sum(1 for a in A if a % 2 == 1)
    even = N - odd
    print(odd * even)