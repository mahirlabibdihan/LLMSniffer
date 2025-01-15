try:
    for _ in range(int(input())):
        s=list(input())
        l=len(s)
        i=l-4
        while i>=0:
            if( ( s[i] == '?' or s[i]=='C') and (s[i+1] == '?' or s[i+1] == 'H') and (s[i+2] == '?' or s[i+2] == 'E') and (s[i+3] == '?' or s[i+3]=='F')):
                s[i] = 'C'
                s[i+1] = 'H'
                s[i+2] = 'E'
                s[i+3] = 'F'
                i -= 4
            else:
                i -= 1
        print("".join(s).replace('?','A'))
except:
    pass