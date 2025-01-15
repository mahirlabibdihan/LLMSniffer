# http://climatecanchange.com/
from itertools import count

for i in range(int(input())):
    k = int(input())
    chef_time = 0
    
    for station in range(k):
        x, l, f = map(int, input().split())
        if station == 0:
            chef_time += x + l
        else:
            for c in count(x, f):
                if c >= chef_time:
                    chef_time = c + l
                    break
            
    print(chef_time)