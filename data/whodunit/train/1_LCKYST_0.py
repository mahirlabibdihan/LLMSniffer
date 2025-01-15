def count_zeroes_at_end(num):
    num=list(str(num))
    ans=0
    while num and num[-1]=='0':
        ans+=1 
        num.pop()  
    return ans

tests=int(input())
num_arr=list(map(int,input().split()))
for num in num_arr:
    ans=num 
    temp=ans*4
    while count_zeroes_at_end(temp)>count_zeroes_at_end(ans):
        ans=temp
        temp*=4
    print(ans)