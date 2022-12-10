buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]

print("Hasil print data buah:")
print(buah)

def copy():
  fruit = buah.copy()
  
  buah[1] = "pepaya"
  buah[2] = "mangga"
  buah[3] = "mangga"
  buah[4] = "pisang"

  fruit[0] = "pisang"
  fruit[1] = "durian"
  fruit[2] = "durian"
  fruit[3] = "jambu"
  fruit[4] = "jambu"

  hasil = buah + fruit

  return hasil

print("\nHasil print duplikasi:")
print(copy())