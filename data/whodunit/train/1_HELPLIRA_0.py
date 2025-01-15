
try:
    def area():
    	n=int(input())
    	b=[]
    	for i in range(n):
    		x1,y1,x2,y2,x3,y3=map(int,input().split())
    		m=abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))
    		b.append(m)
    	p=[i for i, j in enumerate(b) if j == max(b)]
    	q=[i for i, j in enumerate(b) if j == min(b)]
    	print(q[-1]+1,p[-1]+1)
    area()
except:
    pass

