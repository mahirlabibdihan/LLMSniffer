m,c,k = [0]*(10**5+1),[0]*(12000),0
m[1],c[0] = 1,1
for i in range(2,10**5+1):
    j = i
    while j > 0 :
        d = j % 10
        if d == 4 :k += 1
        elif d == 7 :k -= 1
        j //= 10
    m[i] = m[i-1]+ c[k]
    if k == 0 :m[i] += 1
    c[k] += 1
for _ in range(int(input())):print(m[int(input())])