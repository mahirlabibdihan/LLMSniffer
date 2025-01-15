n, m = map(int, input().split())
a = list(map(int, input().split()))
maximum = 1000000000000
final = [False] * n

for i in a:
    final[i - 1] = True

for j in range(1, n):
    test = list(final)
    total = 0
    x = 0
    index = 0
    while x != m and total < maximum:
        if test[index]:
            x += 1
            test[index] = False

        index = (index + j) % n
        total += 1

    if total < maximum: maximum = total
    if maximum == m: break
print(maximum)
