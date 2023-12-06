print("Selamat Datang \n masukan nilai matrik Awal 2x1")

import numpy as np
Nilai_X=float(input("Masukan Nilai X = "))
Nilai_Y=float(input("Masukan Nilai Y = "))
Degree=float(input("Masukan Sudut = "))
Degree=Degree/180*np.pi
P0=np.array([[Nilai_X],
            [Nilai_Y]])
print("P0 = \n",P0)
Rotate=np.array([[np.cos(Degree),-np.sin(Degree)],
                [np.sin(Degree),np.cos(Degree)]])
P1 = Rotate.dot(P0)
print("P1 = \n",P1)