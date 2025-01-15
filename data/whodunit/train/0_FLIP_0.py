T = int(input())
for _ in range(T):
    A = input().strip()
    B = input().strip()
    cnt = [0, 0]
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt[int(A[i])] += 1
    print(max(cnt))