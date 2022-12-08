hasilAkhir = [
  {'Nama':'Reza', 'nilai':70},
  {'Nama':'Ciut', 'nilai':63},
  {'Nama':'Dian', 'nilai':80},
  {'Nama':'Badu', 'nilai':40}
]

print("Daftar Murid Yang Lulus:")
for i in hasilAkhir:
  if(i['nilai'] > 65):
    print(i)