# ashu@gate2022
for i in range(int(input())):
    n=int(input())
    s=input()
    a=input()
    t=0
    j=0
    for i in range(n):
        if j<n:
            if a[j]=="N":
                j+=1
            else:
                if a[j]==s[j]:
                    j+=1
                    t+=1
                else:
                    j+=2
    print(t)

