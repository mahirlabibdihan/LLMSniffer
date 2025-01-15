def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K, M = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        C = sorted(list(map(int, input().strip().split())), reverse=True)
        D = sorted(list(map(int, input().strip().split())), reverse=True)
        tasks = sorted([(A[i] - B[i], i) for i in range(N)], reverse=True)
        i = 0
        while K > 0 and i < N:
            if tasks[i][0] >= C[0]:
                tasks[i] = (tasks[i][0] - C[0], tasks[i][1])
                K -= 1
                C.pop(0)
                if not C:
                    break
            else:
                i += 1
        tasks = sorted(tasks, key=lambda x: x[1])
        i = 0
        while M > 0 and i < N:
            if tasks[i][0] >= D[0]:
                tasks[i] = (tasks[i][0] - D[0], tasks[i][1])
                M -= 1
                D.pop(0)
                if not D:
                    break
            else:
                i += 1
        print(sum([task[0] for task in tasks]))

solve()