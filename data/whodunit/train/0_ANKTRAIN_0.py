T = int(input())
for _ in range(T):
    N = int(input())
    remainder = N % 8
    if remainder == 1:
        print(str(N+3) + "LB")
    elif remainder == 2:
        print(str(N+3) + "MB")
    elif remainder == 3:
        print(str(N+3) + "UB")
    elif remainder == 4:
        print(str(N-3) + "LB")
    elif remainder == 5:
        print(str(N-3) + "MB")
    elif remainder == 6:
        print(str(N-3) + "UB")
    elif remainder == 7:
        print(str(N+1) + "SU")
    else:
        print(str(N-1) + "SL")