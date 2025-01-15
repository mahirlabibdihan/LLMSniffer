for aman in range(int(input())):
    k = int(input())
    if (k == 0):
        print("3")
        continue
    else:
        arr = []
        arr.append("3.")
        r = 103993 % 33102
        for i in range(k):
            r *= 10
            arr.append(r // 33102)
            r = r % 33102
        print(''.join(map(str, arr)))