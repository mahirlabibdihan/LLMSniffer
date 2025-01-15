T = int(input())
for tc in range(T):
    log = input()
    segments = []
    for i in range(len(log)):
        if i % 2 == 0:
            segments.append(log[i:i+2])
    if 'AA' in segments or 'BB' in segments:
        print('no')
    else:
        print("yes")