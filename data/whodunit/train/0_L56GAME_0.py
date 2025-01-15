T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    even_count = sum([1 for i in A if i % 2 == 0])
    odd_count = N - even_count
    print(max(1, odd_count % 2))