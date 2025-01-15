from datetime import datetime, timedelta

def count_pills(T, dates):
    for _ in range(T):
        date = datetime.strptime(dates[_], '%Y:%m:%d')
        day = int(date.strftime('%d'))
        if day % 2 == 0:
            print(day // 2)
        else:
            print(day // 2 + 1)

T = int(input())
dates = []
for _ in range(T):
    dates.append(input())
count_pills(T, dates)