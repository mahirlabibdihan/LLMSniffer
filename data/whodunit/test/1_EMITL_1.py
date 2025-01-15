t=int(input())
for i in range(0,t):
    s=raw_input()
    
    h=[]
    for i in range(0,26):
        h.append(0)
        
    for i in range(0,len(s)):
        x=ord(s[i])-65
        h[x]=h[x]+1
        
    if h[4]>=2 and h[8]>=2 and h[11]>=2 and h[12]>=2 and h[19]>=2:
        print("YES")
    elif len(s)==9 and h[4]==1 and h[8]==2 and h[11]==2 and h[12]==2 and h[19]==2:
        print("YES")
    else:
        print("NO")