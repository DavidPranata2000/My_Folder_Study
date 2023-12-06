import numpy as np
from pyquaternion import Quaternion
print("Selamat Datang \n masukan nilai matrik Awal 3x1")
Nilai_X=float(input("Masukan Nilai X = "))
Nilai_Y=float(input("Masukan Nilai Y = "))
Nilai_Z=float(input("Masukan Nilai Z = "))
P=np.array([[0],
            [Nilai_X],
            [Nilai_Y],
             [Nilai_Z]])
print("P = \n",P)
Nilai_RX=float(input("Masukan Sumbu Putar X = "))
Nilai_RY=float(input("Masukan Sumbu Putar Y = "))
Nilai_RZ=float(input("Masukan Sumbu Putar Z = "))
Degree=float(input("Masukan Sudut = "))
Degree=Degree/180*np.pi
print("Alpha dalam Radian = \n",Degree)
q=Quaternion(axis=[Nilai_RX,Nilai_RY,Nilai_RZ],angle=Degree)
print("q = \n", q)
qC = q.conjugate
print("q* = \n", qC)
P2 = q * P * qC
print("P2 = \n", P2)
P2v2 = q.rotate([Nilai_X,Nilai_Y,Nilai_Z])
print("P2v2 = \n", P2v2)
