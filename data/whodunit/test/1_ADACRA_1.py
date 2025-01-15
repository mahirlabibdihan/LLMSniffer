for _ in range(int(input())):
    s = input()
    sn = []
    sn.append(s[0])
    i = 1
    while i<len(s):
        if s[i] != s[i-1]:
            sn.append(s[i])
        i+=1
    cd = sn.count('D')
    cu = sn.count('U')
    print(min(cd, cu))