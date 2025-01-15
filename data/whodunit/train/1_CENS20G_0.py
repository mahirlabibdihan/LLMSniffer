import io, os, sys
from collections import Counter

def fast_io(): 
    
    # Reinitialize the Input function 
    # to take input from the Byte Like  
    # objects 
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
  
    # Taking input as string  
    s = input().decode() 
    return s 
    
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
s = input().decode()
t = int(s)
#print(t)
for _ in range(t):
    s = input().decode()
    c = Counter(s)
    #print(s)
    #print(input().decode())
    x1, y1 = map(int, input().decode().split())
    #print(x1, y1)
    q = int(input().decode())
    #print(q)
    for i in range(q):
        (x2, y2) = map(int, input().decode().split())
        if (x1, y1) == (x2, y2):
            sys.stdout.write("YES 0\n")
        else:
            dist_x = x1 - x2
            req_x = abs(dist_x)
            dir_x = "R" if dist_x < 0 else "L"
            dist_y = y1 - y2
            req_y = abs(dist_y)
            dir_y = "U" if dist_y < 0 else "D"
            
            count_dir_x = c[dir_x]
            count_dir_y = c[dir_y]
            """
            count_dir_y = 0
            for d in s:
                if d == dir_x:
                    if count_dir_x < req_x:
                        count_dir_x += 1
                elif d == dir_y:
                    if count_dir_y < req_y:
                        count_dir_y += 1
                if count_dir_x >= req_x and count_dir_y >= req_y:
                    break
            """
            if count_dir_x >= req_x and count_dir_y >= req_y:
                sys.stdout.write("YES "+ str(req_x + req_y) + "\n")
            else:
                sys.stdout.write("NO\n")