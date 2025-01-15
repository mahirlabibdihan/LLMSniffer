from math import *
T=int(input())
for i in range(T):
	A,B=list(map(int,input().split(" ")))
	oa=0
	ob=0
	zb=0
	y=0
	r=True
	para=True
	if(A==B):
		print(0)
		r=False
	elif(B==1):
		if(A==0):
			print(1)
			r=False
		else:
			print(-1)
			r=False
	elif(B==0):
		print(-1)
		r=False
	if(r==True):
		io=1		
		while(A>0):
			d=A%2
			oa=oa + d
			A=A//2
		if(B==0):
			zb=1
		else:
			while(B>0):
				y=B%2
				ob=ob + y
				if(para):
					if(y):
						para=False
					else:
						zb+=1
				B=B//2
		fina=ob-oa
		fina1=fina+zb
		if(fina1<=0):
			print(2)
		else:
			print(fina1)	
