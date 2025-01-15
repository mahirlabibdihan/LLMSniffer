t=int(input())
for i in range(t):
	u,v=map(int,input().split())
	x=u+v
	print((x*(x+1)//2)+u+1)