t=int(input())
while t:
    arr=input().strip()
    count=0
    l=len(arr)
    for i in range(l):
        if arr[i] == '4' or arr[i] == '7':
            count+=1
    print(l-count)
    t-=1
    