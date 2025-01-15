T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    even_count = len([i for i in A if i % 2 == 0])
    odd_count = len([i for i in A if i % 2 != 0])
    print(1 if odd_count % 2 else 2)