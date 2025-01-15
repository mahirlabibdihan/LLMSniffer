import math

def min_distance(DS, DT, D):
    if D > DS + DT:
        return D - DS - DT
    elif D + min(DS, DT) < max(DS, DT):
        return max(DS, DT) - D - min(DS, DT)
    else:
        return 0

T = int(input())
for _ in range(T):
    DS, DT, D = map(int, input().split())
    print(min_distance(DS, DT, D))