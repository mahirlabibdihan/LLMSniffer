for _ in range(int(input())):
   k = int(input()) 
   mat = [[0]*k for _ in range(k)]
   start = (k+1)//2 
   for i in range(k):
      for j in range(k):
         val = (start+j)%k
         if val==0: val = k 
         mat[i][j] = val 
      start-=1 
      if start==0:
         start = k 
   for item in mat:
      print(*item)
      
      