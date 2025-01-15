#CHEF AND SOCKS

jc,sc,m = map(int,input().split())

rem_jcm = m-jc
rem_scm = (rem_jcm)//sc

if rem_scm % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
    
