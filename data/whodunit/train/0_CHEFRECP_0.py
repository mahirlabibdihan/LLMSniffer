def chef_recipe(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        A = list(A)
        last = -1
        cnt = [0]*1001
        for i in range(N):
            if i > 0 and A[i] != A[i-1]:
                if cnt[A[i-1]] in cnt[:A[i-1]] or cnt[A[i-1]] in cnt[A[i-1]+1:]:
                    return "NO"
                last = A[i-1]
            cnt[A[i]] += 1
        if cnt[A[N-1]] in cnt[:A[N-1]] or cnt[A[N-1]] in cnt[A[N-1]+1:]:
            return "NO"
        return "YES"

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = map(int, input().split())
    test_cases.append((N, A))
print(chef_recipe(T, test_cases))