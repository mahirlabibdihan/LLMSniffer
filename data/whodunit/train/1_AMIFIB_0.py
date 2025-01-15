# I know I can do this in python
# still want to solve this is c++

a = [0,1]

for i in range (2, 10001):
    a.append(a[i-1] + a[i-2])
    
for t in range (int(input())):
    n = int(input())
    if n in a:
        print("YES")
    else:
        print("NO")
        
#this probably works fine