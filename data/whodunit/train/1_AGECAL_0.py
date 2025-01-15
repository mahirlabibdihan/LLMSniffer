t = int(input())

for i in range(t):
    n = int(input())
    c = 0
    a = list(map(int, input().split()))
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    if y1 != y2:
	    d = a[m1 - 1] - d1 + d2 + 1
	    for j in range(m1, n):
		    d += a[j]
	    for k in range(m2 - 1):
		    d += a[k]
	    d += sum(a) * (y2 - y1 - 1)
	    s = y1
	    while s < y2:
		    if s % 4 == 0:
			    c += 1
		    s += 1 
    else:
	    if m1 == m2:
		    if d1 == d2:
			    d = 1
		    else:
			    d = d2 - d1 + 1
	    else:
		    d = a[m1 - 1] - d1 + d2 + 1
		    for z in range(m1, m2 - 1):
			    d += a[z]
    print(d + c)