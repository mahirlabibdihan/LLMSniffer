test = int(input())

def checkSurvival(n,k,s):
    
    if n<k:
        return -1
    
    elif s>=7 and ((n-k)*6)<k:
        return -1
    
    else:
        choco = k*s
        present = 0
        daysMin = 0
        
        for i in range(1,s+1):
            if i%7!=0:
                present+=n
                daysMin+=1
            else:
                continue
            if present>=choco:
                return daysMin
                
for _ in range(test):
    n,k,s = map(int, input().split())
    
    result = checkSurvival(n,k,s)
    print(result)    