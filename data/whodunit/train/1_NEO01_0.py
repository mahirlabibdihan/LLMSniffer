def max_happiness(arr):
    pos = []
    neg = []
    for y in arr:
        if y > 0:
            pos.append(y)
        else:
            neg.append(y)
    if len(pos) == len(arr):
        return sum(pos)*len(pos)
    elif len(neg) == len(arr):
        return sum(neg)
    else:
        arr.sort()
        arr.reverse()
        i = 0
        s = arr[i]
        current = arr[i]
        j = 1
        while j < len(arr):
            current += arr[j]
            happiness = current*(j - i + 1)
            if happiness >= s:
                s = happiness
                j += 1
            else:
                return s + sum(arr[j: len(arr)])
        return s


test_cases = int(input())
while test_cases != 0:
    data = input()
    data2 = list(map(int, input().split()))
    print(max_happiness(data2))
    test_cases -= 1
