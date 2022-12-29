from animal import *
class elang(animal):
  bentukMulut = ''
  keunggulan = ''
  def __init__(self, name, makanan, hidup, berkembangBiak, bentukMulut, keunggulan):
    super().__init__(name, makanan, hidup, berkembangBiak)
    self.mulut = bentukMulut
    self.ciri = keunggulan

  def printMulut(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nBentuk Mulut \t:', self.mulut)

  def printCiri(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nCiri Khas \t:', self.ciri)