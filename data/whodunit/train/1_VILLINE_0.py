n = int(input())
a = input().split()
m = int(a[0])
c = int(a[1])

t1 = 0
t2 = 0
for _ in range(n):
    b = [int(s) for s in input().split()]
    x = b[0]
    y = b[1]
    p = b[2]
    if y > m*x + c:
        t1 = t1 + p
    else:
        t2 = t2 + p
print(max(t1,t2))