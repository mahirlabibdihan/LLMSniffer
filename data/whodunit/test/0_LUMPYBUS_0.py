def max_creatures(T, test_cases):
    for _ in range(T):
        N, P, Q = test_cases[_][0]
        A = test_cases[_][1]
        A.sort()
        one = [0]*3
        two = [0]*3
        for i in range(N):
            if A[i] % 2 == 0:
                two[(A[i]//2)%3] += 1
            else:
                one[A[i]%3] += 1
        ans = min(P, one[0])
        P -= ans
        temp = min(two[0], Q)
        ans += temp
        Q -= temp
        if P > 1:
            temp = min(two[1], P//2)
            ans += temp
            P -= 2*temp
        temp = min(one[1], P)
        ans += temp
        P -= temp
        if Q > 0:
            temp = min(two[2], Q)
            ans += temp
            Q -= temp
        if P > 1:
            temp = min(one[2], P//2)
            ans += temp
            P -= 2*temp
        print(ans)

T = int(input())
test_cases = []
for _ in range(T):
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, P, Q), A))
max_creatures(T, test_cases)