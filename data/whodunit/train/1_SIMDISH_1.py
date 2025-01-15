for i in range(int(input())):
    s=list(map(str,input().split()))
    a=list(map(str,input().split()))
    l=max(len(a),len(s))
    c=0
    for i in range(l):
        if(s[i] in a):
            c+=1
    if(c>=l//2):
        print('similar')
    else:
        print('dissimilar')