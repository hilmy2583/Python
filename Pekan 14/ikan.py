from animal import *
class ikan(animal):
  jenis = ''
  air = ''
  def __init__(self, name, makanan, hidup, berkembangBiak, jenis, air):
    super().__init__(name, makanan, hidup, berkembangBiak)
    self.jenis = jenis
    self.air = air

  def printJenis(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nJenis Ikan \t:', self.jenis)

  def printAir(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nJenis Air \t:', self.air)