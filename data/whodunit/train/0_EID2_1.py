T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    age = A[:3]
    money = A[3:]
    sorted_pairs = sorted(zip(age, money))
    if sorted_pairs[0][1] <= sorted_pairs[1][1] <= sorted_pairs[2][1] or (sorted_pairs[0][1] == sorted_pairs[1][1] == sorted_pairs[2][1]):
        print("FAIR")
    else:
        print("NOT FAIR")