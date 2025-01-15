for _ in range(int(input())):
	a,b,c,d = map(int , input().split())
	x = c - a
	p = b - a + 1
	q = d - c + 1
	ans = 0
	if(x <= 0):
		t = q - abs(x) - 1
		for j in range(t, max(0,d - b - 1), -1):
			ans += j
	if(x > 0):
		t = q
		for j in range(x, max(0, c - b - 1), -1):
			ans += t
		if(c - b <= 0):
			for j in range(t - 1, max(0, d - b - 1), -1):
				ans += j
	print(ans)