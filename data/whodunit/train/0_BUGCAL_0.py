T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = int(''.join(str(int(i) + int(j)) % 10 for i, j in zip(str(a).zfill(10), str(b).zfill(10))))
    print(result)