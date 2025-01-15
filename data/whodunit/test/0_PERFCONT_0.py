T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    cakewalk = hard = 0
    for i in A:
        if i >= P//2:
            cakewalk += 1
        elif i <= P//10:
            hard += 1
    if cakewalk == 1 and hard == 2:
        print("yes")
    else:
        print("no")