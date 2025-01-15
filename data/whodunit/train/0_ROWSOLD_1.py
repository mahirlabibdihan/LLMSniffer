T = int(input().strip())
for _ in range(T):
    S = input().strip()
    soldiers = [i for i in range(len(S)) if S[i] == '1']
    time = sum(soldiers[i] - i for i in range(len(soldiers)))
    print(time)