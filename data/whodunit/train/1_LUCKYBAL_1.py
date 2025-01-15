for _ in range(int(input())):
    s = input()

    ind, ans = -1, 0

    for i in range(len(s)):
        if s[i] == '4':
            ind = i

        ans += ind+1

    print(ans)    
