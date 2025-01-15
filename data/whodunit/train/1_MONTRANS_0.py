for _ in range(int(input())):
    A, B, C = list(map(int, input().split()))

    seen = set()
    iteration = ans = 0
    max_profit = 100*A + B
    while (A,B) not in seen and (A or B > C):
        seen.add((A,B))
        A, B = (B - C, A) if B >= C else (B + 100 - C, A - 1)
        iteration += 1
        profit = 100*A + B
        if max_profit < profit:
            max_profit = profit
            ans = iteration
        
        #print(A, B, iteration, max_profit)
    print(ans)