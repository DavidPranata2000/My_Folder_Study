from numpy import sin, cos, pi

def kM(el,aa,en=1):
    ex = [0. for ka in range(en+1)]
    ey = [0. for ka in range(en+1)]
    xPrev = 0
    yPrev = 0
    for i in range(0, en):
        ey[i+1] = (sin(aa[i]+aa[i+1])*l[i+1]) + ey[i]
        ex[i+1] = (cos(aa[i]+aa[i+1])*l[i+1]) + ex[i]
    P = [ex[en], ey[en]]
    return P
n = int(input("Tentukan jumlah joint: "))
l = [0. for k in range(n+1)]
a = [0. for k in range(n+1)]
print("Jumlahh joint = ", n)
for j in range(0,n):
    l[j+1] = float(input("Panjang link ke-%i dari titik refrensi: "%(j+1)))
    a[j+1] = float(input("sudut putar joint ke-%i: "%(j+1)))
    a[j+1] = a[j+1] / 180 * pi
endEff=kM(l,a,n)
print("Posisi end efector di koordinat = ",endEff)