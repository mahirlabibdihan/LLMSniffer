n=int(input())
c=n
t=list(map(int,input().split()))

val=0
for i in range(n):
	val+=t[i]
	
tot=n
val-=2*n
if val>0:

	tot+=val//2
	if val%2>0:
		tot+=1
print(tot)	
