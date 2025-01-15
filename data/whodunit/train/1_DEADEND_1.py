def numoftree(arr,n):
    di=dict()
    di[arr[0]]=1 
    count=0
    for i in range(n):
        di[arr[i]]=1 

    for i in range(n):
        if(( arr[i]-1 not in di)and(arr[i]+1 not in di)):
            di[arr[i]+1]=1
            
            count+=1
    return count
t=int(input())
for you in range(t):
    n=int(input())
    l=input().split()
    li=[int(i) for i in l]
    li.sort()
    print(numoftree(li,n))