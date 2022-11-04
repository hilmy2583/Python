print("Masukkan Kondisi Lab Sesuai Keterangan Barikut:")
print("1. lab tersedia")
print("2. lab penuh")
print("3. tidak ada lab")
kondisi = input("Bagaimana Kondisi Lab: ")

if (kondisi == "lab tersedia"):
  ket="Akan Praktikum"
elif (kondisi == "lab penuh"):
  ket="Akan Pindah Jadwal"
elif (kondisi == "tidak ada lab"):
  ket="Tidak Jadi Praktikum"
else:
  print("ERROR")

print('=--------------------------=')
print("Kita", ket)
print('=--------------------------=')