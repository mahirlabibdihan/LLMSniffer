t=int(input())

for _ in range(t):
    n,m=[int(i) for i in input().split()]
    
    (num,den)=(1,1)
    
    for i in range(1,n):
        num=num+den
        den=den+num
        num=num%m
        den=den%m
        
    print(f'{num}/{den}')
	
	
	