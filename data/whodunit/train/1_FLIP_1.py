t = int(input())
for _ in range(t):
    a = input()
    b = input()
    
    v = [False] * len(a)  # Create a boolean list initialized with False
    
    for i in range(len(a)):
        if a[i] != b[i]:
            v[i] = True
    
    count = 0
    
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
    
    print(count)