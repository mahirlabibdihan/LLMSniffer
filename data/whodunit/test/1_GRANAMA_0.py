from collections import Counter
for _ in range(int(input())):
	R,S=input().split()
	B=True
	dr=Counter(list(R))
	ds=Counter(list(S))
	if set(list(R))==set(list(S)):
		for i in set(R):
			if dr[i]!=ds[i]:
				B=False
				break
	if B:
		print('YES')
	else:
		print('NO')