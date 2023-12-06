print("Selamat Datang \n masukan nilai matrik Akhir 2x1")
import numpy as np
Nilai_X=float(input("Masukan Nilai X = "))
Nilai_Y=float(input("Masukan Nilai Y = "))
Degree=float(input("Masukan Sudut = "))
Degree=Degree/180*np.pi
P1=np.array([[Nilai_X],
            [Nilai_Y]])
print("P1 = \n",P1)
Rotate=np.array([[np.cos(Degree),-np.sin(Degree)],
                [np.sin(Degree),np.cos(Degree)]])
Rotate=np.linalg.inv(Rotate)
P0 = Rotate.dot(P1)
print("P0 = \n",P0)