from sys import maxsize
import functools

def customSort(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        if a[1].lower()>b[1].lower():
            return 1
        elif a[1].lower()<b[1].lower():
            return -1
    return 0

def mgc(a,b):
    mp = {}
    for i in b:
        if not i.isalpha():
            continue
        i = i.lower()
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    temp = []
    for i in mp:
        temp.append([mp[i],i])
    temp.sort(key=functools.cmp_to_key(customSort))
    mapped = {}
    i = 25
    j = len(temp)-1
    while(j>=0):
        mapped[temp[j][1]] = a[i]
        j-=1
        i-=1
    ans = ""
    for i in b:
        if i.isupper():
            if i.lower() in mapped:
                ans += mapped[i.lower()].upper()
            continue
        if i in mapped:
            ans += mapped[i]
        else:
            ans += i
    return ans



for i in range(int(input())):
    a = input()
    b = input()
    print(mgc(a,b))
