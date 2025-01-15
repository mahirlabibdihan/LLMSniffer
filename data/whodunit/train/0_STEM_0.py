def find_stem(arr, n):
    s = min(arr, key=len)
    l = len(s)
    res = ""
    for i in range(l):
        for j in range(i + 1, l + 1):
            stem = s[i:j]
            k = 0
            for k in range(1, n):
                if stem not in arr[k]:
                    break
            if (k + 1 == n and len(res) < len(stem)):
                res = stem
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    arr = input().split()
    print(find_stem(arr, n))