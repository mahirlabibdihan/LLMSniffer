T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    correct = [0]*M
    wrong = [0]*M
    invalid = False
    weak = True
    for _ in range(N):
        s, t = input().split()
        t = list(map(int, list(t)))
        if s == "correct":
            if sum(t) != M:
                invalid = True
            for i in range(M):
                correct[i] |= t[i]
        else:
            if sum(t) == M:
                weak = False
            for i in range(M):
                wrong[i] |= t[i]
    if invalid:
        print("INVALID")
    elif weak and correct == wrong:
        print("WEAK")
    else:
        print("FINE")