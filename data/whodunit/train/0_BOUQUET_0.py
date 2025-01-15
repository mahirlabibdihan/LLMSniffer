def max_bouquet(T, test_cases):
    for _ in range(T):
        MG, MY, MR, OG, OY, OR, PG, PY, PR = test_cases[_]
        total = MG + MY + MR + OG + OY + OR + PG + PY + PR
        green = MG + OG + PG
        yellow = MY + OY + PY
        red = MR + OR + PR
        min_color = min(green, yellow, red)
        if total % 2 == 0:
            total -= 1
        if total < min_color * 2:
            total = min((total + 1) // 2 * 2 - 1, total)
        print(total)

T = int(input())
test_cases = []
for _ in range(T):
    MG, MY, MR = map(int, input().split())
    OG, OY, OR = map(int, input().split())
    PG, PY, PR = map(int, input().split())
    test_cases.append((MG, MY, MR, OG, OY, OR, PG, PY, PR))
max_bouquet(T, test_cases)