T = int(input().strip())
for _ in range(T):
    S = input().strip()
    B_count = S.count('B')
    if B_count % 2 == 0:
        print("Chef")
    else:
        print("Aleksa")