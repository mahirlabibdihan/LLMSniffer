def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_pills(T, dates):
    for _ in range(T):
        year, month, day = map(int, dates[_].split(':'))
        if day % 2 == 0:
            print(day // 2)
        else:
            print(day // 2 + 1)

T = int(input())
dates = []
for _ in range(T):
    dates.append(input())
count_pills(T, dates)