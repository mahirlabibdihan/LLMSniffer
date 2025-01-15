def maximize_interaction(T, test_cases):
    for _ in range(T):
        N, K, A, B = test_cases[_]
        interaction = [A[i]*B[i] for i in range(N)]
        interaction.sort(key = lambda x : abs(x))
        i = 0
        while K > 0 and i < N:
            if interaction[i] < 0 and K >= abs(A[i]):
                if B[i] < 0:
                    A[i] += min(K//abs(B[i]), abs(A[i]))
                else:
                    A[i] -= min(K//abs(B[i]), abs(A[i]))
                K -= abs(A[i])
                interaction[i] = A[i]*B[i]
            elif interaction[i] < 0:
                if B[i] < 0:
                    A[i] += K//abs(B[i])
                else:
                    A[i] -= K//abs(B[i])
                K = 0
                interaction[i] = A[i]*B[i]
            elif interaction[i] > 0 and K >= abs(A[i]):
                if B[i] < 0:
                    A[i] -= min(K//abs(B[i]), abs(A[i]))
                else:
                    A[i] += min(K//abs(B[i]), abs(A[i]))
                K -= abs(A[i])
                interaction[i] = A[i]*B[i]
            elif interaction[i] > 0:
                if B[i] < 0:
                    A[i] -= K//abs(B[i])
                else:
                    A[i] += K//abs(B[i])
                K = 0
                interaction[i] = A[i]*B[i]
            i += 1
        print(sum(interaction))

T = int(input().strip())
test_cases = []
for _ in range(T):
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    test_cases.append((N, K, A, B))
maximize_interaction(T, test_cases)