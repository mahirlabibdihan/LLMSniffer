def solve():
    T = int(input())
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        if '1' in B and '1' not in A:
            print("Unlucky Chef")
        else:
            count1 = A.count('1') - B.count('1')
            count0 = A.count('0') - B.count('0')
            print("Lucky Chef")
            print(max(abs(count1), abs(count0)))

solve()