for se in range(int(input())):
    n=int(input());arr = list(map(int,input().split()));l = sorted(arr);i=j=0
    while(i<n and j<n):
        if(l[i]==arr[j]):i,j = i+1,j+1
        else:j=j+1
    print(n-i)    