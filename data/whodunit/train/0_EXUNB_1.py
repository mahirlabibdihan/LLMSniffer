def solve(N):
    if N % 2 == 0:
        return "NO", []
    else:
        result = []
        for i in range(N):
            row = []
            for j in range(N):
                if i == j:
                    row.append(0)
                elif (i - j + N) % N <= N // 2:
                    row.append(1)
                else:
                    row.append(0)
            result.append(row)
        return "YES", result

T = int(input())
for _ in range(T):
    N = int(input())
    res, matrix = solve(N)
    print(res)
    if res == "YES":
        for row in matrix:
            print(''.join(map(str, row)))