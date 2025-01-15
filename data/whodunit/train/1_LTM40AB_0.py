def solve(a , b , c , d):
    x = ( a , min( b , d - 1) )
    y = ( max( c , a + 1 ) , d )
    n = x[1] - x[0] + 1
    m = y[1] - y[0] + 1
    if n < 0 or m < 0:
        ans = 0
    else:
        ans = n * m
        cmn = x[1] - y[0] + 1
        if cmn > 0:
            ans -= (cmn**2 - cmn) // 2
            ans -= cmn
    return ans

T = int(input().strip())
for _ in range(T):
    a , b , c , d = map(int , input().strip().split(' '))
    ans = solve(a , b , c , d)
    print(ans)