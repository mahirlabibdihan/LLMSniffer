n=int(input())

for i in range(n) :
	N,k=map(int,input().split())

	bucks=list(map(int,input().split(' ',N-1)))
	ans=0
	mid=int(k/2)
	for j in bucks :
		x=j%k
		y=k-x
		if j>=k:
			ans=ans+min(x,y)
		else:
			ans=ans+y

	print(ans)	