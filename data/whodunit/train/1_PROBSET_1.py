def cd(n):
    c=0
    for x in n:            
        if x=='1':
            c+=1
    return c
for _ in range(int(input())):
	m,n=map(int,input().split())
	inv,we,f=0,0,0
	for _ in range(m):
		a,b=map(str,input().split())
		if a[0]=='c':
			if cd(b)!=n:inv=1
		elif a[0]=='w':
			if cd(b)==n:we=1
	if inv==1:print('INVALID')
	elif we==1 and inv==0:print('WEAK')
	elif inv==0 and we==0:print('FINE')
