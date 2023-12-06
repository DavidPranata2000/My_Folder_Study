Jumlah_A=int(input("Masukan Jumlah Bilangan A ="))
Data_A = []
for i in range(Jumlah_A):
    Nilai_A=int(input(f"masukan data ke-{i + 1}: "))
    Data_A.append(Nilai_A)
Data_A = set(Data_A)
print("Bilangan A = ",Data_A)
Jumlah_B=int(input("Masukan Jumlah Bilangan B ="))
Data_B = []
for i in range(Jumlah_B):
    Nilai_B=int(input(f"masukan data ke-{i + 1}: "))
    Data_B.append(Nilai_B)
Data_B = set(Data_B)
print("Bilangan B = ",Data_B)
print("Silahkan pilih")
print("u = gabungan")
print("n = irisan")
Pilihan=input("Silahkan Masukan Pilihan : ")
if Pilihan == "u" or Pilihan == "U":
    Gabungan=Data_A | Data_B
    Hasil_Akhir=Gabungan
elif Pilihan == "n" or Pilihan == "N":
    Iris=Data_A & Data_B
    Hasil_Akhir=Iris
else :
    Hasil_Akhir="Anda salah memilih bilangan"
print(Hasil_Akhir)