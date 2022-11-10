#variabel
plite = 10000
pmax = 14000
pturbo = 17000

jtempuh_plite = 12
jtempuh_pmax = 13
jtempuh_pturbo = 13.5

Jakarta = 20
Bekasi = 35.7
Depok = 5
Tangerang = 99
Bogor = 120.6

#input
print("Jenis Kendaraan:")
print("1. Motor")
print("2. Mobil")
kendaraan = input("Nama Kendaraan: ")
print("Jenis Bensin:")
print("1. Pertalite")
print("2. Pertamax")
print("3. Pertamax Turbo")
bensin = input("Jenis Bensin: ")
print("Kota:")
print("1. Jakarta")
print("2. Bekasi")
print("3. Depok")
print("4. Tangerang")
print("5. Bogor")
tujuan = input("Kota Tujuan: ")

#proses
if (bensin == "pertalite" or bensin == "Pertalite") :
  pemakaian = eval(tujuan) / jtempuh_plite
  hasil = pemakaian * plite
elif (bensin == "pertamax" or bensin == "Pertamax") :
  pemakaian = eval(tujuan) / jtempuh_pmax
  hasil = pemakaian * pmax
elif (bensin == "pertamax turbo" or bensin == "Pertamax Turbo") :
  pemakaian = eval(tujuan) / jtempuh_pturbo
  hasil = pemakaian * pturbo
else :
  print("Error")

#output
print("Nama Kendaraan       :", kendaraan)
print("Jenis Bensin         :", bensin)
print("Kota yang dituju     :", tujuan)
print("Bensin yang digunakan:", pemakaian, "Liter")
print("Total Pembayaran     :", "Rp", hasil)