T = int(input())
for _ in range(T):
    N = input().strip()
    digits = [0]*10
    for i in N:
        digits[int(i)] += 1
    ans = [0]*26
    for i in range(10):
        if digits[i] > 0:
            for j in range(i, 10):
                if digits[j] > 0:
                    num = i*10 + j
                    if num >= 65 and num <= 90:
                        ans[num-65] = 1
    for i in range(26):
        if ans[i] == 1:
            print(chr(i+65), end='')
    print()