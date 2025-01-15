import collections 
n,m=map(int,input().split())
arr=[int(i) for i in input().split()]
e=collections.deque(arr)
for j in range(m):
    s,k=map(str,input().split())
    k=int(k)
    result=[]
    if s=='R':
        print(e[k-1]) 
         
    elif s=='C':
        e.rotate(-k)
        
    elif s=='A':
        e.rotate(k) 


    
        