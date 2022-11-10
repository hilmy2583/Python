nama_pembeli = input("Masukkan Nama Anda: ")
no_hp_pembeli = int(input("Masukkan No Handphone Anda: "))
pemesanan = input("Mau Pesan Apa? ")
if (pemesanan == "makanan" or pemesanan == "Makanan"):
  print("Dartar Menu Makanan: \n 1. Nasi Goreng \n 2. Mie Goreng \n 3. Ayam Geprek")
elif (pemesanan == "minuman" or pemesanan == "Minuman"):
  print("Dartar Menu Minuman: \n 1. Aneka Jus \n 2. Soft Drink \n 3. Sweet Ice Tea")
else:
  print("Error")
menu = input("Masukkan Pesanan Anda: ")
jumlah = int(input("Masukkan Jumlah Pemesanan: "))
if (menu == "Nasi Goreng" or menu == "Aneka Jus"):
  harga = 15000 * jumlah
elif (menu == "Mie Goreng"):
  harga = 12000 * jumlah
elif (menu == "Ayam Geprek"):
  harga = 18000 * jumlah
elif (menu == "Soft Drink"):
  harga = 10000 * jumlah
elif (menu == "Sweet Ice Tea"):
  harga = 5000 * jumlah

#output
print("Nama             :", nama_pembeli)
print("No Handphone     :", no_hp_pembeli)
print("Menu yang dipesan:", menu)
print("Jumlah Pesanan   :", jumlah)
print("Harga Total      :", "Rp", harga)