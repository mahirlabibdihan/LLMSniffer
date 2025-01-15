for case in range(int(input())):
    A = 10**9
    B = 10**9
    for i in range(int(input())):
        s = input()
        A = min(A, sum(c == 'a' for c in s))
        B = min(B, sum(c == 'b' for c in s))
    print(min(A, B))