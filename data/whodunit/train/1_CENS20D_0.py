for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    c = 0
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == (s[i] & s[j]):
                c += 1
    else:
        print(c)