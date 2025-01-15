for _ in range(int(input())):
	X=int(input())
	l=[0,1]
	while True:
		p=len(l)+l[-1]
		l.append(p)
		if p>X:
			break
	t1=len(l)-1+l[-1]-X
	t2=len(l)-2+X-l[-2]
	print(min(t1,t2))
		
		