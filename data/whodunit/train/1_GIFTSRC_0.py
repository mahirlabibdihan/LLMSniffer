for _ in range(int(input())):
    n = int(input())
    s = input()
    pos = [0,0]
    prev = ''
    for l in s:
        if l == 'R' or l == 'L':
            if prev == 'R' or prev == 'L':
                continue
            elif l == 'R':
                pos[0] += 1
            else:
                pos[0] -= 1
        elif l == 'U' or l == 'D':
            if prev == 'U' or prev == 'D':
                continue
            elif l == 'U':
                pos[1] += 1
            else:
                pos[1] -= 1        
        prev = l                
    print(*pos)            
            