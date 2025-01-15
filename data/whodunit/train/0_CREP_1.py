T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    unique_numbers = set(A)
    result = sum(number for number in unique_numbers if A.count(number) == K)
    print(result if result != 0 else -1)