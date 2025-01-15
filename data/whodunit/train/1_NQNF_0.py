import numpy as np
n,q=map(int,input().split())
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))
for i in range(q):
	query=list(map(int,input().split()))
	if query[0]==1:
		print(np.amax(a[query[1]-1:query[2]]))
	if query[0]==2:
		a[query[1]-1:query[2]]+=b[query[1]-1:query[2]]
	if query[0]==3:
		b[query[1]-1:query[2]]+=query[3]
	if query[0]==4:
		a[query[1]-1:query[2]]+=query[3]
	