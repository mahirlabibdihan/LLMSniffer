from sys import stdin
tc=int(stdin.readline())
for i in range(tc):
    n=int(stdin.readline())
    list1=[]
    for j in range(n):
        s1=stdin.readline()
        list1.append(s1)
    f_n=[1]*n
    f_e=[1]*n
    count=0
    for k in range(n-1,-1,-1):
        for l in range(n-1,-1,-1):
            if list1[k][l]=="#":
                f_n[k]=0
                f_e[l]=0
            elif f_e[l] and f_n[k]:
                count+=1
    print(count)
    