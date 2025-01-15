for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a == b:
        result = -1
    else:
        diff = abs(a-b)
        result = 1 + (diff > 1)
        for i in range(2, diff):
            j = i*i
            if j < diff:
                if diff % i == 0:
                    result += 2
                continue
            if j == diff:
                result += 1
            break
    print(result)
    