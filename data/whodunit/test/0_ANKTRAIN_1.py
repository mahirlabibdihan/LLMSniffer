T = int(input())
for _ in range(T):
    N = int(input())
    berth = {1: "LB", 2: "MB", 3: "UB", 4: "LB", 5: "MB", 6: "UB", 7: "SL", 0: "SU"}
    remainder = N % 8
    if remainder in [1, 2, 3]:
        print(str(N+3) + berth[remainder])
    elif remainder in [4, 5, 6]:
        print(str(N-3) + berth[remainder])
    elif remainder == 7:
        print(str(N+1) + berth[remainder])
    else:
        print(str(N-1) + berth[remainder])