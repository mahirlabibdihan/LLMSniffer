T = int(input())
for _ in range(T):
    N = input().strip()
    digits = [0]*10
    for i in N:
        digits[int(i)] += 1
    ans = []
    for i in range(10):
        if digits[i] > 0:
            for j in range(i, 10):
                if digits[j] > 0:
                    num = i*10 + j
                    if num >= 65 and num <= 90:
                        ans.append(chr(num))
    ans.sort()
    print(''.join(ans))