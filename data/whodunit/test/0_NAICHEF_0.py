T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    x = list(map(int, input().split()))
    pA = x.count(A) / N
    pB = x.count(B) / N
    print('{:.15f}'.format(pA * pB))