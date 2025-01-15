for _ in range(int(input())):
    N, C, Q = map(int,input().split())
    for i in range(Q):
        L, R = map(int,input().split())
        if C <= R and C >= L:
            C = L + R - C
    print(C)