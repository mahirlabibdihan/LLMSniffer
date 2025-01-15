for _ in range(int(input())):
    N=int(input())
    direc=[]
    for _ in range(N):
        direc.append(input().split())
    the_reverse=[]
    for i in range(N):
        the_reverse.append(direc[N-i-1])
    invert=[]
    for i in range(N-1):
        this_seq=the_reverse[i]
        prev_key=this_seq[0]
        if prev_key=='Left':
            invert.append('Right')
        else:
            invert.append('Left')
    for i in range(1,N):
        the_reverse[i][0]=invert[i-1]
    the_reverse[0][0]='Begin'
    for row in the_reverse:
        print(' '.join(row))