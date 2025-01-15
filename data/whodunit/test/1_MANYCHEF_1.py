for _ in range(int(input())):
    s=list(input())
    l=len(s)
    i=l-1
    while i>=0:
        if (i>=3) and  ((s[i]=='F' or s[i]=='?') and (s[i-1]=='E' or s[i-1]=='?') and (s[i-2]=='H' or s[i-2]=='?') 
            and (s[i-3]=='C' or s[i-3]=='?')):
            s[i-3:i+1]='C','H','E','F'
            i-=4
            
        else:
            if s[i]=='?':
                s[i]='A'
                
            i-=1
            
    print(''.join(s))
            
            
    