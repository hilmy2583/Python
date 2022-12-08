def potong(isi):
  hapus = ['a', 'i', 'u', 'e','o', ' ']
  hasil = ''

  for i in isi:
    # print(hasil)
    if i not in hapus:
      hasil += i
  return hasil

print(potong('Nurul Fikri'))