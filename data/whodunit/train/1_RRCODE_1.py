from functools import reduce
ops = {"XOR": lambda x,y : x^y, "AND": lambda x,y : x&y, "OR": lambda x,y : x|y}
for _ in range(int(input())):
    n, k, ans = map(int, input().split())
    arr = list(map(int, input().split()))
    op = input().strip()
    tot = reduce(ops[op], arr)
    if k == 0:
        print (ans)
        continue
    if op == "XOR":
        if k % 2 == 0:
            print (ans)
        else:
            print (ans ^ tot)
    elif op == "AND":
        print (ans & tot)
    else:
        print (ans | tot)