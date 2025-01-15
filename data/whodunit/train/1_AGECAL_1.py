t=int(input())
j=0
while(j<t):
	n=int(input())
	leap=0
	a= [int(i) for i in input().split()]
	y1,m1,d1=map(int,input().split())
	y2,m2,d2=map(int,input().split())
	if(y1!=y2):
		days=a[m1-1]-d1+d2+1
		for i in range(m1,n):
			days=days+a[i]
		for i in range(0,m2-1):
			days=days+a[i]
		days=days+sum(a)*(y2-y1-1)
		i=y1
		while(i<y2):
			if(i%4==0):
				leap=leap+1
			i=i+1
	else:
		if(m1==m2):
			if(d1==d2):
				days=1
			else:
				days=d2-d1+1
		else:
			days=a[m1-1]-d1+d2+1
			#print(a[m1-1])
			#print(d1)
			#print(d2)
			for i in range(m1,m2-1):
				days=days+a[i]
				
			
			
			
	print(days+leap)
	j=j+1
	