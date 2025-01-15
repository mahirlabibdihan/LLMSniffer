from math import ceil
def fun(n):
	if(n==1):
		print(1)
		return
	ans= (n/2)+0.5
	x=ceil(n-1-ans)
	seq= list(range(1+x,1+x+n))
	print(*seq)
test=int(input())
for i in range(test):
	n=int(input())
	fun(n)