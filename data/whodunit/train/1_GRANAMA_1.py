T = int(input())
for i in range(T):
  r, s = input().split()
  r = list(r)
  s = list(s)
  r.sort()
  s.sort()
  if set(r) == set(s):
    t = "YES"
  else:
    t = "NO"
  if r == s and len(r) == len(s):
    c = "YES"    
  else:
    c = "NO"
  if t == c:
    print("YES")
  else:
    print("NO")