T = int(input().strip())
for _ in range(T):
    S = input().strip()
    last_soldier = S.rfind('1')
    time = 0
    for i in range(last_soldier):
        if S[i] == '1':
            time += last_soldier - i
            last_soldier -= 1
    print(time)