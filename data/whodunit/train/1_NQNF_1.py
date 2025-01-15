import numpy as np
n,q = map(int,input().split())
a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))
ans = []
for i in range(q):
	query = tuple(map(int,input().split()))
	if len(query)==3:c,l,r = query
	else: c,l,r,x = query
	if c==1:
		ans.append(np.max(a[l-1:r]))
	elif c==2:
		a[l-1:r]+=b[l-1:r]
	elif c==3:
		b[l-1:r]+=x
	else:
		a[l-1:r]+=x
print(*ans,sep="\n")