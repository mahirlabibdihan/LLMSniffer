def ammeat2(n, k):
	if k == 1:
		print(1)
	elif k > n // 2:
		print(-1)
	else:
		start = 1
		while k:
			print(start*2, end=' ')
			start += 1
			k -= 1
		print()
		
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ammeat2(n, k)