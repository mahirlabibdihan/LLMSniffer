T = int(input())

def RightTriangle(H,S):
    
    if (H**2-4*S)<0:
        return -1
    
    a = (H**2+4*S)**0.5
    b = (H**2-4*S)**0.5
    c = (a+b)/2
    d = (a-b)/2
    
    if c<=0 and d<=0:
        return -1
    else:
        e = str(d)+' '+str(c)+' '+str(H)
        return e
    
for i in range(T):
    H,S = map(int,input().split())
    
    print(RightTriangle(H,S))