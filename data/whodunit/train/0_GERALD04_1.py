T = int(input())
for _ in range(T):
    time1 = sum(int(x) * 60 ** i for i, x in enumerate(input().strip().split(":")[::-1]))
    time2 = sum(int(x) * 60 ** i for i, x in enumerate(input().strip().split(":")[::-1]))
    dist = int(input())
    if time1 >= time2 + 2*dist:
        print("%.1f %.1f" % (time1 - time2, time1 - time2))
    else:
        print("%.1f %.1f" % (time1 - time2 + (2*dist - time1 + time2)/2, time1 - time2 + dist))