from math import sqrt
for i in range(int(input())):
    P,A=map(int,input().split())
    l = (P - sqrt(P * P - 24 * A)) / 12; 
    V = l * (A / 2.0 - l * (P / 4.0 - l)); 
    print("%.2f"%(V))