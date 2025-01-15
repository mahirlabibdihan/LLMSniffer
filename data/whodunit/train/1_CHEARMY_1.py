def MagicalNum(k):
    if 1 <= k <= 5:
        return 2*(k-1) 
    elif k == 0:
        return 0
    elif k % 5 == 0:
        v1 = k // 5
        return 10*MagicalNum(v1) + 8
    else:
        v1 = k//5
        v2 = k % 5
        return 10*MagicalNum(v1 + 1) + MagicalNum(v2)     
T = int(input())
for _ in range(T):
    k = int(input())
    print(MagicalNum(k))