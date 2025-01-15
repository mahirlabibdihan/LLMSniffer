T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    max_product = max_rating = max_index = -1
    for i in range(n):
        if L[i]*R[i] > max_product or (L[i]*R[i] == max_product and R[i] > max_rating):
            max_product = L[i]*R[i]
            max_rating = R[i]
            max_index = i
    print(max_index + 1)