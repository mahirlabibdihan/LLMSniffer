n = int(input())
arr = list(map(int,input().split()))
lds = []
for i in arr:
    lo,hi = 0,len(lds)
    while lo<hi:
        mid = (lo+hi)>>1
        if i<lds[mid]:lo=mid+1
        else: hi=mid
    if lo==len(lds): lds.append(i)
    else: lds[lo] = i
print(len(lds))
