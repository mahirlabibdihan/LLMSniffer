def can_divide_stamps(n, stamps):
    total_stamps = sum(stamps)
    required_stamps = n * (n + 1) // 2
    if total_stamps == required_stamps:
        return "YES"
    else:
        return "NO"

n = int(input())
stamps = list(map(int, input().split()))
print(can_divide_stamps(n, stamps))