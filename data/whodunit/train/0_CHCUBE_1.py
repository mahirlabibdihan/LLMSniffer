T = int(input().strip())
for _ in range(T):
    colors = input().strip().split()
    color_set = set(colors)
    for color in color_set:
        if colors.count(color) >= 2:
            print("YES")
            break
    else:
        print("NO")