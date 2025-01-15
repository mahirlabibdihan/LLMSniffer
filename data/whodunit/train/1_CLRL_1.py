try:
    for _ in range(int(input())):
    	N,R=input().split()
    	N,R=int(N),int(R)
    	A=[int(j) for j in input().split()]
    	l,r=0,max(A)+1
    	for i in range(N):
    		if A[i]>R and A[i]<r:
    			r=A[i]
    		elif A[i]<R and A[i]>l:
    			l=A[i]
    		else:
    			if A[i]==R:
    				print("YES")
    				break
    			else:
    				print("NO")
    				break
except:
    pass