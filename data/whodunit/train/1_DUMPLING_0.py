def gcd(a,b):
  if(a%b == 0):
    return b
  return gcd(b, a%b)
    
for T in range(int(input())):
    A, B, C, D, K = [int(x) for x in input().split()]
    GCD_1 = gcd(B,A)
    GCD_2 = gcd(D,C)
    GCD = gcd(max(GCD_1,GCD_2),min(GCD_1,GCD_2))
    LCM = (GCD_1*GCD_2)//GCD
    count = int(K//LCM)
    count *= 2
    count += 1
    print(count)