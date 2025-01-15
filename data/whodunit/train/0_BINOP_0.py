def solve():
    T = int(input())
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        if '1' in B and '1' not in A:
            print("Unlucky Chef")
        else:
            count1 = sum(a!=b for a,b in zip(A,B) if a=='1')
            count0 = sum(a!=b for a,b in zip(A,B) if a=='0')
            print("Lucky Chef")
            print(max(count1, count0))

solve()