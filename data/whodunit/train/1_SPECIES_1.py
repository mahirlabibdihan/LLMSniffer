import sys
sys.setrecursionlimit((10**7))
from collections import defaultdict
def Neigh(i,j,N):
    L=[]
    if(i+1 !=N):
        L.append([i+1,j])
    if(j+1 !=N):
        L.append([i,j+1])
    if(i!=0):
        L.append([i-1,j])
    if(j!=0):
        L.append([i,j-1])
    return L
    
def chngneigh(Arr,i,j,target):
    ll=Neigh(i,j,N)
    next=[]
    for x in ll:
        if(Arr[x[0]][x[1]]=="?"):
            Arr[x[0]][x[1]]=target
            next.append(x)
    for x in next:
        Arr=chngneigh(Arr,x[0],x[1],target)
    return Arr
    
for _ in range(int(input())):
    N=int(input())
    Mat=[]
    for _ in range(N):
        row=list(input())
        Mat.append(row)
    for i in range(N):
        for j in range(N):
            if(Mat[i][j]=="P"):
                Mat=chngneigh(Mat,i,j,"P")
            elif(Mat[i][j]=="B"):
                Mat=chngneigh(Mat,i,j,"B")
    fine=True
    for i in range(N):
        for j in range(N):
            if(Mat[i][j]=="." or Mat[i][j]=="?"):
                pass
            elif(Mat[i][j]=="G"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]!="."):
                        fine=False
                        break
            elif(Mat[i][j]=="P"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]=="B" or Mat[x[0]][x[1]]=="G" ):
                        fine=False
                        break
            elif(Mat[i][j]=="B"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]=="P" or Mat[x[0]][x[1]]=="G" ):
                        fine=False
                        break
        if(fine==False):
            break
    if(fine==False):
        print("0")
        continue
    else:
        solo=0
        for i in range(N):
            for j in range(N):
                if(Mat[i][j]=="?"):
                    ll=Neigh(i,j,N)
                    yup=True
                    for x in ll:
                        if(Mat[x[0]][x[1]]!="."):
                            yup=False
                    if(yup==True):
                        solo+=1
                        Mat[i][j]="D"
        clustor=0
        for i in range(N):
            for j in range(N):
                if(Mat[i][j]=="?"):
                    Mat=chngneigh(Mat,i,j,"c")
                    clustor+=1
        answer=pow(3,solo,1000000007)*pow(2,clustor,1000000007)
        print(answer%1000000007)