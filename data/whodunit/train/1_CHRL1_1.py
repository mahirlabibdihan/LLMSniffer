def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
  
t=int(input())
for i in range(t):
    wt=[]
    val=[]
    n,k=map(int,input().split())
    for i in range(n):
        x,y=map(int,input().split())
        wt.append(x)
        val.append(y)
    print(knapSack(k,wt,val,n))