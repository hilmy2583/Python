buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]

print(buah)

def balik():
  fls = []
  for i in range(len(buah)):
    revers = len(buah) - 1 - i
    fls.append(buah[revers])
  return fls

print(balik())