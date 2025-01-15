t= int(input())
for x in range(t):
    s=input()
    lst=[]
    count = 0
    for i in range(len(s)-1):
        if s[i:i+2] in lst:
            pass
        else:
            lst.append(s[i:i+2])
            count+=1
    print(count)