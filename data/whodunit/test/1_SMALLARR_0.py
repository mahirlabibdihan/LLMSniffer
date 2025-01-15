n,k=map(int, input().split())
arr=list(map(int, input().split()))
sum_arr=[0]*n
sum_arr[0]=arr[0]
partial=arr[0]

for i in range(1,n):
    partial+=arr[i]
    sum_arr[i]=partial
    
sum_arr.insert(0,0)    

max_var=sum_arr[1]-sum_arr[0]

for i in range(1,n+1):
    for j in range(i):
        if (max_var<=(sum_arr[i]-sum_arr[j])):
            max_var=(sum_arr[i]-sum_arr[j])
            
print('%0.1f' %(sum(arr)+(max_var)*((1/k)-1)))