for _ in range(int(input())):
	N=int(input())
	A=list(map(int,input().split()))
	s=A[0]
	for i in range(N-1):
		if A[i+1]>A[i]:
			s+=A[i+1]-A[i]
	print(s)