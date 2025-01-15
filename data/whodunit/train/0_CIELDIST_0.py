T = int(input())
for _ in range(T):
    DS, DT, D = map(int, input().split())
    if D > DS + DT:
        print(D - DS - DT)
    elif D + min(DS, DT) < max(DS, DT):
        print(max(DS, DT) - D - min(DS, DT))
    else:
        print(0)