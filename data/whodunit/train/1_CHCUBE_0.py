def check(s1,s2,s3):
    if(s1==s2 and s2==s3 and s3==s1):
        return True
    else:
        return False
for _ in range(int(input())):
    f,b,l,r,t,bo = input().split()
    if(check(f, t, l) or check(f, t, r) or check(f,bo, l) or check(f,bo, r) or check(b, t, l) or check(b, t, r) or check(b, bo, l) or check(b, bo, r)):
        print("YES")
    else:
        print("NO")