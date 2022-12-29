class animal:
  name = ''
  makanan = ''
  hidup = ''
  berkembangBiak = ''
  def __init__(self, name, makanan, hidup, berkembangBiak):
    self.nama = name
    self.makan = makanan
    self.habitat = hidup
    self.reproduksi = berkembangBiak

  def printAnimal(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi)