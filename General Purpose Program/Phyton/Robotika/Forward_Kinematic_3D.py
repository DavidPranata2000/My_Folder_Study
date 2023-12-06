from numpy import sin, cos, pi, array, eye, dot
from numpy.linalg import multi_dot
def TransZ(de,en=1):
    Di = [0. for ka in range(en)]
    for i in range(0, en):
        Di[i] =  array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,de[i]],
                        [0,0,0,1]])
    return Di

def TransX(aa,en=1):
    Ai = [0. for ka in range(en)]
    for i in range(0, en):
        Ai[i] =  array([[1,0,0,aa[i]],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]])
    return Ai

def RotZ(te,en=1):
    Ti = [0. for ka in range(en)]
    for i in range(0, en):
        Ti[i]=([[cos(te[i]),-sin(te[i]),0,0],
                [sin(te[i]),cos(te[i]),0,0 ],
                [0,0,1,0],
                [0,0,0,0]])
    return Ti
def RotX(aa,en=1):
    Ai = [0. for ka in range(en)]
    for i in range(0, en):
        Ai[i]=([ [1,0,0,0],
                 [0,cos(aa[i]),-sin(aa[i]),0],
                 [0,sin(aa[i]),cos(aa[i]),0 ],
                 [0,0,0,1]])
    return Ai
def Trans(rotx,rotz,transx,transz,en=1):
    TT= [0. for ka in range(en)]
    for i in range(0, en):
        TT[i]= multi_dot([rotx[i],rotz[i],transz[i]])
        print("Trans ke-", i, " = ",TT[i])
    return TT

def TransTotal(TT,en=1):
    TransTot=eye(4)
    for i in range(0, en):
        TransTot=dot(TransTot,TT[i])
        print("Perkalian Trans ke-",i, " = ",TransTot)
    return TransTot
n=int(input("Tentukan Jumlah joint: "))
d =[0. for k in range(n)]
a =[0. for k in range(n)]
t =[0. for k in range(n)]
alp =[0. for k in range(n)]
print("Jumlah joint = ",n)
for j in range(0, n):
    a[j]=float(input("Panjang link ke-%i ($a_%i$): "%(j+1,j+1)))
    d[j]=float(input("Panjang d ke-%i: "%(j+1)))
    t[j]=float(input("Sidit $\(theta)$ ke-%i: "%(j+1)))
    t[j]=t[j]/180*pi
    alp[j]=float(input("Sudut $\(alpha)$ ke-%i: "%(j+1)))
    alp[j]=alp[j]/180*pi
print("Theta i = ",t)
tz=TransZ(d,n)
tx=TransX(a,n)
rz=RotZ(t,n)
rx=RotX(alp,n)
Tr=Trans(rx,tx,rz,tz,n)
T=TransTotal(Tr,n)
P=[T[0,3],T[1,3],T[2,3]]
print("Trans Z = ",tz)
print("Trans X = ",tx)
print("Rot Z = ",rz)
print("Rot X = ",rz)
print("Trans Total = ",T)
print("Posisi end effector = ",P)

    




        
