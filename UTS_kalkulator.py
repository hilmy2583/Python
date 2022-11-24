Tambah = "+"
Kurang = "-"
Bagi = ":"
Kali = "x"
Pangkat = "^"
tambah = "+"
kurang = "-"
bagi = ":"
kali = "x"
pangkat = "^"

angka_pertama = float(input("Masukkan angka 1: "))
angka_kedua = float(input("Masukkan angka 2: "))

print("Operator = Keterangan")
print("   +     = Tambah")
print("   -     = Kurang")
print("   /     = Bagi")
print("   *     = Kali")
print("   **    = Pangkat")
print("________________________")
operasi = input("Masukkan Jenis Keterangan: ")

if (operasi == "+" or operasi == "Tambah" or operasi == "tambah"):
  hasil = angka_pertama + angka_kedua
elif (operasi == "-" or operasi == "Kurang" or operasi == "kurang"):
  hasil = angka_pertama - angka_kedua
elif (operasi == "/" or operasi == "Bagi" or operasi == "bagi"):
  hasil = angka_pertama / angka_kedua
elif (operasi == "*" or operasi == "Kali" or operasi == "kali"):
  hasil = angka_pertama * angka_kedua
elif (operasi == "Pangkat" or operasi == "pangkat"):
  hasil = angka_pertama ** angka_kedua

print("________________________")
print("Angka Pertama    :", angka_pertama)
print("Angka Kedua      :", angka_kedua)
print("Pilihan Operator :", operasi)
print("Hasil Operator", angka_pertama, eval(operasi), angka_kedua, "=", hasil)
print("________________________")