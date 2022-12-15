# memanggil dan menjalankan modul P12modulBangunDatar
print("====================Modul Bangun Datar====================")
import P12modulBangunDatar as hasil
hasil.lingkaran(14)
hasil.persegi(5)
hasil.persegiPanjang(5, 3)
hasil.segitiga(4, 7)
hasil.belahKetupat(4, 5)

print(" ")
print(" ")
print(" ")
print(" ")

from P12modulAritmatika import tambah, kurang, kali
print("=====================Modul Aritmatika=====================")
bil1 = int(input("Masukkan Bilangan Pertama: "))
bil2 = int(input("Masukkan Bilangan Kedua : "))
tambah(bil1, bil2)
kurang(bil1, bil2)
kali(bil1, bil2)