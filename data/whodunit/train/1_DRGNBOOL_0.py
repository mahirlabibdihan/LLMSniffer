t = int(input())
for i in range(0,t):
	n,m = map(int, input().split())
	soi = {}
	sof = {}
	for j in range (0,n):
		c, l = map(int, input().split())
		if not (l in soi.keys()):		
			soi[l]  = c	
		else:
			soi[l] += c 

	for j in range (0,m):
		c, l = map(int, input().split())
		if not (l in sof.keys()):		
			sof[l] = c
		else:
			sof[l] += c
	sum=0
	for i in soi.keys():
		if soi[i] < sof[i]:
			sum += sof[i] - soi[i]
	
	print(sum)