#Program Menghitung Berat Badan Ideal
#input
print('======================================================')
print('======================================================')
tinggi_badan = input('Masukkan Tinggi badan(centimeter): ')

#rumus
berat_badan_ideal = (int(tinggi_badan) - 100) - ((int(tinggi_badan) - 100) * 10 / 100)

#output
print('==============================================')
print("Berat badan ideal dari tinggi", tinggi_badan, "adalah:", berat_badan_ideal)
print('======================================================')
print('======================================================')