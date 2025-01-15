def isLeap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False


DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


ntests = int(input())

for test in range(ntests):
    year, month, day = map(int, input().split(':'))
    count = 0

    if month == 2:
        if isLeap(year):
            count = (29 - day) // 2 + 1
        else:
            count = (59 - day) // 2 + 1
    elif DAYS[month] == 31:
        count = (31 - day) // 2 + 1
    else:
        count = (61 - day) // 2 + 1

    print(count)










