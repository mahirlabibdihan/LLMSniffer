try:
    for i in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        m_list=[]
        t_list=[]
        for j in range(0,len(l)):
            if(j%2==0):
                m_list.append(l[j])
            else:
                t_list.append(l[j])
        for k in range(k):
            max_m=max(m_list)
            min_t=min(t_list)
            max_index=m_list.index(max_m)
            min_index=t_list.index(min_t)
            t_list.append(max_m)
            m_list.append(min_t)
            m_list.pop(max_index)
            t_list.pop(min_index)
    
        if(sum(t_list)>sum(m_list)):
            print("YES")
        else:
            print("NO")
        
        
        
        
        
except:
    pass