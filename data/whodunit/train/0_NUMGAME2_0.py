T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1 or N % 2 == 0:
        print("BOB")
    else:
        print("ALICE")