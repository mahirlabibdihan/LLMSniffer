
t = int(input())

for i in range(t):
    n = int(input())
    
    if 360%n == 0:
        print("y",end=' ')
    else:
        print("n",end=' ')
    
    if n>360:
        print("n",end=' ')
    else:
        print("y",end=' ')
    
    if (n*(n+1))/2 <= 360:
        print("y",end=' ')
    else:
        print("n",end=' ')
        
    print('')