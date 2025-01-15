t=int(input())
for _ in range(t):
  s=input()
  n=len(s)
  if n==1 and s[0]=='?':
    print(26)
  else:
    count=1
    left=0
    right=n-1
    while left<=right:
      if s[left]=="?" and s[right]=="?":
        left+=1
        right-=1
        count=(count*26)%10000009
      elif s[left]=='?' or s[right]=='?' or s[left]==s[right]:
        left+=1
        right-=1
        continue
      else:
        count=0
        break
    print(count)