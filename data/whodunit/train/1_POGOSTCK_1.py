for _ in range (int(input())):
	n, m = map(int, input().split())
	l = list(map(int, input().split()))
	#print(l)
	l1 = []
	if m > n:
		print(max(l))
	else:
		for i in range (m):
			a = l[i]
			for j in range (i + m, n, m):
				a = max((l[j] + a), l[j])
				#print(l[i], l[j])
			l1.append(a)
		print(max(l1))
	