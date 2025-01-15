from collections import *
for u in range(int(input())):
    l=input().split()
    C=l
    if C[0]==C[2]==C[4] or C[0]==C[2]==C[5] or C[0]==C[3]==C[4] or C[0]==C[3]==C[5] or C[1]==C[2]==C[4] or C[1]==C[2]==C[5] or C[1]==C[3]==C[4] or C[1]==C[3]==C[5]:  
        print('YES')
    else:
        print('NO')        