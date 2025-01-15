for i in range(int(input())):
  s = input()
  n = len(s)
  arr = [0]*n
  for i in range(n):
    arr[i] = int(s[i])
  total = 0
  count = 0
  lastIdx = n-1
  curr = n-1
  while(arr[curr]==1 and curr>=0):
    lastIdx-=1
    curr-=1
  while curr>=0:
    if arr[curr]==1:
      if arr[curr+1]==0:
        count+=1
      total+=count+(lastIdx-curr)
      lastIdx-=1
    curr-=1
  print(total)