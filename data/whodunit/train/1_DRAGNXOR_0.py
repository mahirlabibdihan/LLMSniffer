for tc in range(int(input())):
    
    z,n1,n2 = map(int,input().split(' '))
    
    n1 = bin(n1)
    n2 = bin(n2)
    
    c1 = n1.count('1')
    c2 = n2.count('1')
    
    ones =  c1+c2
    
    nums = abs(z - ones)
    
    sumi = 0 
    for i in range(nums,z):
        sumi = sumi + 2**i
        
        
    print(sumi)