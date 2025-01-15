t = int(input())
 
for _ in range(t):
	
	# n, k  = list(map(int, input().split()))
	# lst = list(map(int, input().split()))
	n = int(input())


	n = n - 1

	mul = 1 
	res = 0

	while n:
		res += 2*(n%5)*mul
		n = n//5
		mul *= 10
	print(res)