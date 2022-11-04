#Program Mengkonversi Suhu
#input
print('======================================================')
print('======================================================')
celcius = input('Masukkan derajat suhu celcius: ')

#rumus
fahreinheit = (int(celcius) * 9 / 5) + 32
reamur = (int(fahreinheit) - 32) * 4 / 9

#output
print('======================================================')
print("Suhu pada Celcius     :", celcius)
print("Suhu pada Fahreinheit :", fahreinheit)
print("Suhu pada Reamur      :", reamur)
print('======================================================')
print('======================================================')