test=int(input())
for _ in range(test):
	n=int(input())
	a=list(map(int,input().split()))
	c=0
	c2=0
	for i in range(n):
		if a[i]==2:
			c2+=1
		elif a[i]>2:
			c+=1
	res=int((c2*c)+((c*(c-1))/2))
	print(res)
