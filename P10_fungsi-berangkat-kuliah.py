def berangkat_kuliah(kondisi_cuaca):
  if(kondisi_cuaca == "hujan" or kondisi_cuaca == "Hujan" or kondisi_cuaca == "HUJAN"):
    pergi = "Berangkat naik Gocar"
  elif(kondisi_cuaca == "adem" or kondisi_cuaca == "Adem" or kondisi_cuaca == "ADEM"):
    pergi = "Berangkat naik motor"
    
  print("Cuaca hari ini %s, maka %s" %(kondisi_cuaca, pergi))

berangkat_kuliah("Hujan")
berangkat_kuliah("ADEM")