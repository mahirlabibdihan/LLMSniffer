import math
t = int(input())
for tc in range(0,t):
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	
	cur = 0
	ans = 0
	
	for i in range(0,n):
		if a[i] < cur:
			cur = cur - a[i]
		else:
			x = math.ceil((a[i] - cur)/k)
			ans = ans + int(x)#convert x to int so that answer is an integer
			cur = cur + (x * k - a[i])
		if cur > 0:
			cur = cur - 1
	print(ans)#the final answer should be an integer amount of packages