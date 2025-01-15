def find_stem(arr, n):
    s = min(arr, key=len)
    l = len(s)
    res = ""
    for i in range(l):
        for j in range(i + 1, l + 1):
            stem = s[i:j]
            if all(stem in word for word in arr):
                if len(stem) > len(res) or (len(stem) == len(res) and stem < res):
                    res = stem
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    arr = input().split()
    print(find_stem(arr, n))