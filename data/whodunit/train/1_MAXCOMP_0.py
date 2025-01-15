for _ in range(int(input())):
	N = int(input())
	R = [0 for x in range(49)]
	A = []
	for k in range(N):
		st =input().split()
		S = int(st[0])
		E = int(st[1])
		C = int(st[2])
		A.append([S,E,C])
	A.sort()
	for x in A:
		S = x[0]
		E = x[1]
		C = x[2]
		nc = R[S] + C
		if nc > R[E]:
			for k in range(E,49):
				if nc > R[k]:
					R[k] = nc
	print(R[48])