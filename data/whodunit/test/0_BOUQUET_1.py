def max_bouquet(T, test_cases):
    for _ in range(T):
        MG, MY, MR, OG, OY, OR, PG, PY, PR = test_cases[_]
        green = MG + OG + PG
        yellow = MY + OY + PY
        red = MR + OR + PR
        maple = MG + MY + MR
        oak = OG + OY + OR
        poplar = PG + PY + PR
        total = [green, yellow, red, maple, oak, poplar]
        total.sort()
        ans = total[-1]
        if ans % 2 == 0:
            ans -= 1
        print(ans)

T = int(input())
test_cases = []
for _ in range(T):
    MG, MY, MR = map(int, input().split())
    OG, OY, OR = map(int, input().split())
    PG, PY, PR = map(int, input().split())
    test_cases.append((MG, MY, MR, OG, OY, OR, PG, PY, PR))
max_bouquet(T, test_cases)