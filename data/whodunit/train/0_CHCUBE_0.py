T = int(input().strip())
for _ in range(T):
    colors = input().strip().split()
    if colors.count(colors[0]) >= 2 or colors.count(colors[2]) >= 2 or colors.count(colors[4]) >= 2:
        print("YES")
    else:
        print("NO")