'''MAXEP: SUBMISSION BY PRIYANSHU SHARMA
18 FEBRUARY,2019'''
from sys import stdin as inp
from sys import stdout as out
n,coins=map(int,input().split())
l=1
r=n
while r-l>0:
	key=(7*l+r)//8
	print(1,key)
	out.flush()
	res=int(input())
	inp.flush()
	if res==0:
		l=key+1
	else:
		r=key
		print(2)
		out.flush()
print(3,l)
out.flush()