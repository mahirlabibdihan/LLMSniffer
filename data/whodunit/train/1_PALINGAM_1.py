t=int(raw_input())
for j in range(t):
    a,b=raw_input(),raw_input()
    ta,tb=set(a),set(b)
    for i in ta:
        if a.count(i) > 1 and i not in tb:
            print('A')
            break
    else: 
        if len(ta)-len(tb) > 0:
            if len(tb)-len(ta) > 0:
                print('B')
            else:
                print('A')
        else:
            print('B')