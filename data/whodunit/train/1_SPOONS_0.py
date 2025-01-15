f = [0] * 70
f[0] = 1
ans = [1]
for i in range(1, 70, 1):
    f[i] = i * f[i - 1]
for i in range(2,70,1):
    ans.append(f[i] // (f[i // 2] * f[i - (i // 2)]))
    
t = int(input())

for i in range(t):
    n = int(input())
    for j in range(70):
        if ans[j] >= n:
            print(j + 1)
            break   