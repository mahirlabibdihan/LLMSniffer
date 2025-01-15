T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.remove(max(A))
    B.remove(max(B))
    sum_A = sum(A)
    sum_B = sum(B)
    if sum_A < sum_B:
        print("Alice")
    elif sum_A > sum_B:
        print("Bob")
    else:
        print("Draw")