T = int(input())
for _ in range(T):
    A = input().strip()
    B = input().strip()
    cnt0, cnt1 = 0, 0
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
    print(max(cnt0, cnt1))