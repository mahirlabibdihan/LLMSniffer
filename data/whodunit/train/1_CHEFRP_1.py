for _ in range(int(input())):
	n = int(input())
	items = list(map(int,input().split()))
	if min(items) < 2:
		total = -1
	else:
		total = sum(items) - min(items) + 2
	print(total)
