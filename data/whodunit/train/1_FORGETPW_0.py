case=int(input())
for _ in range(case):
    n = int(input())
    replacement = {}
    for i in range(n):
        v,r = input().split(" ")
        replacement[v] = r
    s = input()
    news = ""
    point = False
    for i in range(len(s)):
        if s[i] in replacement:
            if replacement[s[i]]=='.':
                point = True
            news+=replacement[s[i]]
        else:
            if s[i]=='.':
                point = True
            news+=s[i]
    
    i = 0
    while i<len(news):
        if news[i]!='0':
            break
        i+=1
    news = news[i:]
    if point:
        j = len(news)-1
        while j>=0:
            if news[j]!='0':
                break
            j-=1
        if j>=0 and news[j]=='.':
            j-=1
        news = news[:j+1]
    if len(news)==0:
        print(0)
    else:
        print(news)
        