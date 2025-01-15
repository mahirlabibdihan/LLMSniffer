for _ in range(int(input())):
	st=input().split()
	N=int(st[0])
	M=int(st[1])
	valid=False
	if N*M==2:
		valid=True
	if (N*M%2==0) and (min(N,M)>1):
		valid=True
	if valid:
		print('Yes')
	else:
		print('No')