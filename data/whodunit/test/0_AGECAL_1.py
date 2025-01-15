def is_leap_year(year):
    return year % 4 == 0

def solve():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        days_in_month = list(map(int, input().strip().split()))
        yb, mb, db = map(int, input().strip().split())
        yc, mc, dc = map(int, input().strip().split())
        total_days = 0
        for year in range(yb, yc + 1):
            if is_leap_year(year):
                total_days += sum(days_in_month) + 1
            else:
                total_days += sum(days_in_month)
        total_days -= sum(days_in_month[mb - 1:]) + db - 1
        if is_leap_year(yb) and mb == N:
            total_days -= 1
        total_days -= sum(days_in_month[:mc - 1]) + (days_in_month[mc - 1] - dc)
        if is_leap_year(yc) and mc == N:
            total_days += 1
        print(total_days)

solve()