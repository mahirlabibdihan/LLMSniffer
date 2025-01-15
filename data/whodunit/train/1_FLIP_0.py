def minOperations(a, b):
    count = 0
    v = [False] * len(a)

    for i in range(len(a)):
        if a[i] != b[i]:
            v[i] = True

    for i in range(len(v)):
        if v[i]:
            count += 1
        else:
            continue

        j = i + 2
        while j < len(v):
            if v[j]:
                v[j] = False
            else:
                break
            j += 2

    return count

def main():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()

        result = minOperations(a, b)
        print(result)

if __name__ == "__main__":
    main()
