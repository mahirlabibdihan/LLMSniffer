def magical_number(k):
    return int(format(k, 'b')) * 5

t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    print(magical_number(k))