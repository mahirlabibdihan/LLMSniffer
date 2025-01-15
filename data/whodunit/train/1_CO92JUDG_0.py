for i in range(int(input())):
	x=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	a.sort()
	b.sort()
	a.pop(-1)
	b.pop(-1)
	c=sum(a)
	d=sum(b)
	if c>d:
		print('Bob')
	elif d>c:
		print('Alice')
	elif c==d:
		print('Draw')