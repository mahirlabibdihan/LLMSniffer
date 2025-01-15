from math import * 

t=int(input())

def func(y,t):
    return y*t - int( (t*(t+1)*(2*t+1))/6)


for alpha in range(t):
    y=int(input())
    t=int(sqrt(y))
    ans = func(y,t)
    
    if y<=701:
        print(ans)
        continue
    else:
        z=int(sqrt(y-700))
        ans=ans + 700 * z
        ans = ans - func(y,z)
        print(ans)