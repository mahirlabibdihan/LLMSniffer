from operator import mul
from functools import reduce


def binom_n_6(n, mod):
    x = reduce(mul, [n-i for i in range(6)]) % mod
    y = pow(reduce(mul, range(1,7)), mod-2, mod)
    return (x * y) % mod    
   
   
mod = 10**9 + 7
n = int(input())
#print(n)

if n < 13:
    count = 0
else:
    # Find number of different combinations
    # comb of length 7 with sum(comb) == (n+1)//2
    theSum = (n+1)//2
    """
    count = 0
    for a1 in range(1, theSum - 5):
        for a2 in range(a1 + 1, theSum - 4):
            for a3 in range(a2 + 1, theSum - 3):
                for a4 in range(a3 + 1, theSum - 2):
                    for a5 in range(a4 + 1, theSum - 1):
                        for a6 in range(a5 + 1, theSum - 0):
                            print(a1, a2, a3, a4, a5, a6, 
                                  #theSum - sum([a1, a2, a3, a4, a5, a6])
                                  )
                            count += 1
    count = summands(theSum, 7, mod)
    if n % 2 == 1:
        pass
    """
    count = binom_n_6(theSum - 1, mod)
    
print(count)
    