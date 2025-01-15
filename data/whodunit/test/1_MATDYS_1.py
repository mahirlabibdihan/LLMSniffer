t = int(input())
for _ in range(t):
	n, k = list(map(int, raw_input().split()))
	k += 1
	i = n-1
	ans = 0
	while(i >= 0):
		if (k > 2**i):
			ans += 2**(n-1-i)
			k -= 2**i
		i -= 1
	print(ans)