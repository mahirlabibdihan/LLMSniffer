def chef_drinks_coke_2():
    n, m, k, l, r = [int(x) for x in input().split()]    
    min = 10000000 
    for i in range(n):
        c, p = [int(x) for x in input().split()]                       

        for j in range(m):
            if c>k+1:
                c -= 1                
            elif c<k-1:
                c += 1                
            else:
                c = k


        if c>=l and c<=r:
            if p<min:
                min = p                
    
    if min!=10000000:
        print(min)
    else:
        print(-1)

t = int(input())
while t>0:
    chef_drinks_coke_2()
    t-=1