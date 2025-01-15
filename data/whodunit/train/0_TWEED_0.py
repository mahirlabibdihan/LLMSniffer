T = int(input().strip())
for _ in range(T):
    N, P = input().strip().split()
    N = int(N)
    heaps = list(map(int, input().strip().split()))
    if P == "Dee" and max(heaps) % 2 == 0:
        print("Dee")
    else:
        print("Dum")