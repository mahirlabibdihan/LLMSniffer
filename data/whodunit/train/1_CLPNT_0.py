import bisect

'''
def find_wall(list_wall,num_wall,xi,yi):
    left=0;
    right=num_wall
    while left<right:
        mid=(left+right)//2
        if yi<list_wall[mid]-xi:
            right=mid
        elif yi==list_wall[mid]-xi:
            return mid
        else:
            left=mid+1
    return left
'''

T=int(input())

for _ in range(T):
    N=int(input())
    ai=list(map(int,input().split()))
    Q=int(input())
    for _ in range(Q):
        x,y=map(int,input().split())
        ind=bisect.bisect_left(ai,x+y)
        if ind==N:
            print(N)
        elif ai[ind]==x+y:
            print("-1")
        else:
            print(ind)
        '''
        pos=find_wall(ai,N,x,y)
        if pos==N:
            print(N)
        elif y==ai[pos]-x:
            print("-1")
        else:
            print(pos)
        '''