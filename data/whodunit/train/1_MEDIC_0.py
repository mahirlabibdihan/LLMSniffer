try:
    months_31 = [1, 3, 5, 7, 8, 10, 12]

    def leap_year(year):
        if  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    t = int(input())
    for _ in range(t):
        y, m, d = map(int, input().split(':'))
        count = 0
        if m in months_31:
            count = (31 - d) // 2 + 1
        elif m == 2:
            if leap_year(y):
                count = (29 - d) // 2 + 1
            else:
                if d % 2 == 0:
                    count = (28 - d) // 2 + 1 + 15
                else:
                    count = (28 - d) // 2 + 1 + 16
        else:
            if d % 2 == 0:
                count = (30 - d) // 2 + 1 + 15
            else:
                count = (30 - d) // 2 + 1 + 16
        print(count)
except:
    pass