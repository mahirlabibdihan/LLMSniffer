t = int(input())

while t!=0:
    s1 = input()
    s2 = input()
    
    s = s1.split(':')
    t1 = (int(s[0])*60)+int(s[1])
    s = s2.split(':')
    t2 = (int(s[0])*60)+int(s[1])
    
    t3 = int(input())
    
    if(t1-t2>=2*t3):
        ans2 = t1-t2
    else:
        ans2 = (t1-t2)+(2*t3+t2-t1)/2
    
    ans1 = t1-t2+t3;
    
    print('%0.1f %0.1f' %(ans1, ans2))
    t-=1