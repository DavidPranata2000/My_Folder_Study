print("Selamat Datang \n masukan nilai matrik Awal 3x1")
import numpy as np
Nilai_X=float(input("Masukan Nilai X = "))
Nilai_Y=float(input("Masukan Nilai Y = "))
Nilai_Z=float(input("Masukan Nilai Z = "))
P0=np.array([[Nilai_X],
            [Nilai_Y],
             [Nilai_Z]])
print("P0 = \n",P0)
AXIS=input("Rotasi Terhadap Sumbu = ")
Degree=float(input("Masukan Sudut = "))
Degree=Degree/180*np.pi
if AXIS == "X" or AXIS == "x":
  Rotate=np.array([[1,0,0],
                [0,np.cos(Degree),-np.sin(Degree)],
                [0,np.sin(Degree),np.cos(Degree)]])
elif AXIS == "Y" or AXIS == "y":
  Rotate=np.array([[np.cos(Degree), 0, np.sin(Degree)],
                [0, 1, 0],
                [-np.sin(Degree), 0, np.cos(Degree)]])
elif AXIS == "Z" or AXIS == "z":
  Rotate=np.array([[np.cos(Degree), -np.sin(Degree), 0],
                [np.sin(Degree), np.cos(Degree), 0],
                [0, 0, 1]])
else :
  print("Anda salah/tidak memasukan AXIS")
P1 = Rotate.dot(P0)
print("P1 = \n",P1)