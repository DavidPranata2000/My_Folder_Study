import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

Kurva_Awal = int(input("Masukkan titik Awal Kurva: "))
Kurva_Akhir = int(input("Masukkan titik Akhir Kurva: "))

# Generate x values
x_qual = np.arange(Kurva_Awal, Kurva_Akhir, 0.1)
print("Awal Kurva =", Kurva_Awal, "\nAkhir Kurva =", Kurva_Akhir)

print("Pilih Jumlah titik yang diinginkan (2 titik,3 titik,4 titik)")
Jumlah_Titik=int(input("Masukan Jumlah titik ="))
# Generate the triangular membership function with 4 points
if Jumlah_Titik > 2:
    Grafik_Awal = int(input("Masukkan titik sebelum Kurva Naik(Titik 1) : "))
    Grafik_Akhir = int(input(f"Masukkan titik setelah kurva Turun (Titik {Jumlah_Titik}): "))
else:
    Grafik_Akhir = int(input(f"Masukkan titik setelah kurva Naik/Turun (Titik {Jumlah_Titik}): "))
if Jumlah_Titik==2:
    Jenis_Kurva=input("Masukan Jenis Kurva(Naik/Turun) : ")
    if Jenis_Kurva == "Naik" or Jenis_Kurva == "naik" or Jenis_Kurva == "NAIK":
        qual_lo = sk.trimf(x_qual, [Grafik_Akhir, Kurva_Akhir,Kurva_Akhir])
    elif Jenis_Kurva == "Turun" or Jenis_Kurva == "turun" or Jenis_Kurva == "TURUN":
        qual_lo = sk.trimf(x_qual, [0, 0,Grafik_Akhir])
    else:
        qual_lo = sk.trimf(x_qual, [0,0,0])
elif Jumlah_Titik == 3:
    Grafik_Puncak= int(input("Masukkan titik awal Kurva Puncak(Titik 2) : "))
    qual_lo = sk.trimf(x_qual, [Grafik_Awal, Grafik_Puncak,Kurva_Akhir])
elif Jumlah_Titik == 4:    
    Grafik_Puncak_Awal = int(input("Masukkan titik awal Kurva berada di puncak(Titik 2) : "))
    Grafik_Puncak_Akhir = int(input("Masukkan titik akhir Kurva berada di puncak(Titik 3) : "))
    qual_lo = sk.trapmf(x_qual, [Grafik_Awal, Grafik_Puncak_Awal,Grafik_Puncak_Akhir,Grafik_Akhir])
else:
    qual_lo = sk.trimf(x_qual, [0,0,0])    

# Plot the membership function
plt.plot(x_qual, qual_lo, label='Fungsi Keanggotan')
threshold_value = 0.5  # Ganti nilai sesuai kebutuhan
plt.axhline(threshold_value, color='red', linestyle='--', label='Threshold')

# Customize the plot
plt.title('Membership Function')
plt.xlabel('Quality')
plt.ylabel('Membership Degree')
plt.legend()

# Show the plot
plt.show()
