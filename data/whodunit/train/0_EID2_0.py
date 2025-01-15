T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    B = sorted([(A[i], A[i+3]) for i in range(3)])
    if B[0][1] < B[1][1] <= B[2][1] or B[0][1] == B[1][1] == B[2][1]:
        print("FAIR")
    else:
        print("NOT FAIR")