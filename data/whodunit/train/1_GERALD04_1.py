def gerald04(time1, time2, dist):
	wait = (int(time1[3:])-int(time2[3:])) + (int(time1[:2])-int(time2[:2]))*60
	first = wait + dist
	if dist <= wait - dist:
		second = wait
	else:
		second = dist + wait / 2
	return float(first), float(second)
	
t = int(input())
for _ in range(t):
    time1 = input()
    time2 = input()
    dist = int(input())
    a, b = gerald04(time1, time2, dist)
    print(a, b)