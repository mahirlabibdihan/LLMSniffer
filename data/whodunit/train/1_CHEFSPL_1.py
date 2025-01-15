for case in range(int(input())):
    s = input()
    n = len(s)//2
    if len(s)==1:
        print('NO')
    elif len(s)%2==0:
        print('YES' if (s[0:n]==s[n:]) else 'NO')
    else:
        match = True
        skip = 0
        for i in range(n):
            if s[i+skip]!=s[i+n+1]:
                if skip==1 or s[i+1]!=s[i+n+1]:
                    match = False
                    break
                skip = 1
        if match:
            print('YES')
            continue
        match = True
        skip = 0
        for i in range(n):
            if s[n-1-i]!=s[2*n-i-skip]:
                if skip==1 or s[n-1-i]!=s[2*n-i-1]:
                    match = False
                    break
                skip = 1
        if match:
            print('YES')
        else:
            print('NO')