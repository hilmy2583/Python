from animal import *
class ular(animal):
  serangan = ''
  sisik = ''
  def __init__(self, name, makanan, hidup, berkembangBiak, serangan, sisik):
    super().__init__(name, makanan, hidup, berkembangBiak)
    self.serangan = serangan
    self.corak = sisik

  def printSerang(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nBentuk Serangan :', self.serangan)

  def printCorak(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t:', self.makan,
          '\nHabitat \t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nCorak Sisik \t:', self.corak)