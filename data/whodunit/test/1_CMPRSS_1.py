def printOutput(isFirst, s, sl):
    if isFirst==False:
        print(',',end='')
    if sl>2:
        print(str(s) + '...' + str(s+sl-1),end='')
    elif sl==2:
        print(str(s) + ',' + str(s+1),end='')
    else:
        print(str(s),end='')

tc = int(input())
for i in range(tc):
    n = int(input())
    x = input().split()
    s=int(x[0])
    sl=1
    isFirst = True
    for j in range(1,n):
        if int(x[j])==s+sl:
            sl = sl + 1
        else:
            printOutput(isFirst,s,sl)
            isFirst=False
            s = int(x[j])
            sl = 1
        if j==n-1:
            printOutput(isFirst,s,sl)
    if n==1:
        printOutput(isFirst,s,sl)
    print('')
