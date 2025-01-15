for _ in range(int(input())):
	a,b,c=map(int,input().split())
	if (a+b<=c):print("{:.4f}".format(round(c-(a+b),5)))
	else:
		if(max(a,b)>c+min(a,b)):print("{:.4f}".format(round(max(a,b)-(c+min(a,b)),5)))
		else:print(0.0000)