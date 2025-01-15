def fun(a,n):
    b=['cakewalk','simple','easy'],
    if 'cakewalk' in a  and 'simple' in a and 'easy' in a and ('easy-medium' in a or 'medium' in a) and ('medium-hard' in a or 'hard' in a):
        print('Yes')
    else:
        print('No')
        
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(input())
    fun(a,n)