for t in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	c,v=0,0
	for i in l:
		if l.count(i)>c:
			c=l.count(i)
			v=i
	print(v,c)