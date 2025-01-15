import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    a = s.split()
    min_string  = min(a,key=len)
    length = 0
    sub_str = ""
    length_sub_str = 0
    longest_sub_str = ""
    for i in range(0,len(min_string)):
        for j in range(i+1,len(min_string)+1):
            sub_str = min_string[i:j]
            flag = False
            for ele in a:
                if(sub_str in ele):
                    flag = True
                else:
                    flag = False
                    break
            if(flag == True):
                if(length_sub_str < len(sub_str)):
                    length_sub_str = len(sub_str)
                    longest_sub_str = sub_str
                elif(length_sub_str == len(sub_str)):
                    if(longest_sub_str > sub_str):
                        longest_sub_str = sub_str
    print(longest_sub_str)
            
    