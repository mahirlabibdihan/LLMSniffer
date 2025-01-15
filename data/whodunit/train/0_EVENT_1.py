def solve():
    T = int(input().strip())
    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    for _ in range(T):
        S, E, L, R = input().strip().split()
        L = int(L)
        R = int(R)
        start = days.index(S)
        end = days.index(E)
        duration = (end - start + 1) % 7
        if duration < L:
            duration += 7
        if duration > R:
            print("impossible")
        elif L <= duration <= R:
            if duration + 7 <= R:
                print("many")
            else:
                print(duration)
        else:
            print("impossible")

solve()