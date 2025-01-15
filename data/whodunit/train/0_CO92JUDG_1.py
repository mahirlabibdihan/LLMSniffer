T = int(input())
for _ in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    A.pop()
    B.pop()
    sum_A = sum(A)
    sum_B = sum(B)
    if sum_A < sum_B:
        print("Alice")
    elif sum_A > sum_B:
        print("Bob")
    else:
        print("Draw")