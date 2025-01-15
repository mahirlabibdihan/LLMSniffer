T = int(input())
for _ in range(T):
    time1 = list(map(int, input().split(':')))
    time2 = list(map(int, input().split(':')))
    dist = int(input())
    time1 = time1[0]*60 + time1[1]
    time2 = time2[0]*60 + time2[1]
    if time1 >= time2 + 2*dist:
        print("%.1f %.1f" % (time1 - time2, time1 - time2))
    else:
        print("%.1f %.1f" % (time1 - time2 + (2*dist - time1 + time2)/2, time1 - time2 + dist))