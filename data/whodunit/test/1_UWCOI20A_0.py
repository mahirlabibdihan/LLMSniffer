n = int(input())

for i in range(n):
    l = [0]
    k = int(input())
    
    for j in range(k):
        
        m = int(input())
        if(m>l[-1]):
            l.append(m)
            
    
    print(l[-1])