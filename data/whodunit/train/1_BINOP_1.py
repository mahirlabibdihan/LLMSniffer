from sys import stdin,stdout
out=stdout.write
raw_input=stdin.readline
for i in range(int(raw_input())):
        a=list(raw_input().strip('\n'));a1='';b1=''
        b=list(raw_input().strip('\n'));m=0;n=0
        for i in range(len(a)):
            if a[i]!=b[i]:n+=1;a1+=a[i];b1+=b[i]
        l1=a1.count('1');l=a1.count('0');l2=min(l,l1)
        if a.count('1')==0 or a.count('0')==0:out("Unlucky Chef\n")
        else:n-=2*l2;m+=l2+n;out("Lucky Chef\n"+str(m)+'\n')