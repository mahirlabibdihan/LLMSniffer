T = int(input().strip())
for _ in range(T):
    S = input().strip()
    if '01' in S and '10' in S:
        print("NO")
    else:
        print("YES")