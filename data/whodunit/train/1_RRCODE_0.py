import functools
for _ in range(int(input())):
    n,k,ans=map(int,input().split())
    l=list(map(int,input().split()))
    op=input().strip()
    if k>0:
        # AND
        if op[0]=='A':
            for i in range(len(l)):
                ans=ans&l[i]
            print(ans)
        #OR
        elif op[0]=='O':
            for i in range(len(l)):
                ans=ans|l[i]
            print(ans)
        #XOR
        else:
            if k%2==0:
                print(ans)
            else:
                for i in range(len(l)):
                    ans=ans^l[i]
                print(ans)
    elif(k==0):
        print(ans)