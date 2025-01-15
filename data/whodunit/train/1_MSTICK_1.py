N=int(input())
arr=[int(x) for x in input().split()]

MAXN=100005
seg=[0]*(4*MAXN)
seg1=[0]*(4*MAXN)


def build(node,ss,se):

    if(ss==se):
        seg[node]=arr[ss]
        return arr[ss]

    mid=(ss+se)>>1
    build(2*node+1,ss,mid)
    build(2*node+2,mid+1,se)

    seg[node]=min(seg[2*node+1],seg[2*node+2])


def build1(node,ss,se):

    if(ss==se):
        seg1[node]=arr[ss]
        return arr[ss]

    mid=(ss+se)>>1
    build1(2*node+1,ss,mid)
    build1(2*node+2,mid+1,se)

    seg1[node]=max(seg1[2*node+1],seg1[2*node+2])


    
def getmin(node,ss,se,qs,qe):

    if(qs>se or qe<ss or qs>qe):
        return 1000000000000000000000000000

    if(qs<=ss and qe>=se):
        return seg[node]

    mid=(ss+se)>>1
    return min(getmin(2*node+1,ss,mid,qs,qe),getmin(2*node+2,mid+1,se,qs,qe))


def getmax(node,ss,se,qs,qe):

    if(qs>se or qe<ss or qs>qe):
        return 0

    if(qs<=ss and qe>=se):
        return seg1[node]

    mid=(ss+se)>>1
    return max(getmax(2*node+1,ss,mid,qs,qe),getmax(2*node+2,mid+1,se,qs,qe))





build1(0,0,N-1)
build(0,0,N-1)


Q=int(input())
for i in range(0,Q):
    L,R=map(int,input().split())

    t1=getmax(0,0,N-1,0,L-1)
    t2=getmax(0,0,N-1,R+1,N-1)
    t3=getmin(0,0,N-1,L,R)
    t4=getmax(0,0,N-1,L,R)

    ans=t3+max(t1/1,t2/1,(t4-t3)/2)
    print(ans)
    
