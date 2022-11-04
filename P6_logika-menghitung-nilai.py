nama = input("Masukkan Nama Anda: ")
kelas = input("Masukkan Kelas Anda: ")
nilai = int(input("Masukkan Nilai Anda: "))

if (nilai >= 90):
  ket="Istimewa"
elif (nilai >= 70):
  ket="Sangat Bagus"
elif (nilai >= 60):
  ket="Cukup"
else:
  ket="Gagal"

print("Nama       :", nama)
print("Kelas      :", kelas)
print("Nilai      :", nilai)
print("Keterangan :", ket)