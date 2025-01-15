t= int(input())
while t:
    t-=1
    n=int(input())
    str1=input()
    str2=input()
    arr=list(map(int,input().split()))
    c_cor=0
    for i in range(n):
        if str1[i]==str2[i]:
            c_cor+=1
    if c_cor==n:
        print(arr[-1])
    else:
        print(max(arr[:c_cor+1:]))