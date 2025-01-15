def can_divide_stamps(n, stamps):
    total_stamps = 0
    for stamp in stamps:
        total_stamps += stamp
    required_stamps = n * (n + 1) // 2
    if total_stamps == required_stamps:
        return "YES"
    else:
        return "NO"

n = int(input())
stamps = list(map(int, input().split()))
print(can_divide_stamps(n, stamps))