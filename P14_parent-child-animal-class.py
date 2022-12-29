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
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi)

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
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nJenis Ikan \t\t\t:', self.jenis)

  def printAir(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nJenis Air \t\t\t:', self.air)

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
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nBentuk Mulut \t\t:', self.mulut)

  def printCiri(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nCiri Khas \t\t\t:', self.ciri)

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
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nBentuk Serangan :', self.serangan)

  def printCorak(self):
    print('\nData', self.nama,
          '\nNama Binatang \t:', self.nama,
          '\nMakanan \t\t\t\t:', self.makan,
          '\nHabitat \t\t\t\t:', self.habitat,
          '\nBerkembang Biak :', self.reproduksi,
          '\nCorak Sisik \t\t:', self.corak)

animal1 = animal('Kijang', 'Herbivora', 'Padang Rumput', 'Melahirkan')
ikan1 = ikan('Ikan', 'Plankton', 'Laut', 'Melahirkan', 'Hiu Paus', 'Air Asin')
ikan2 = ikan('Ikan Gurame', 'Cacing', 'Danau', 'Bertelur', 'Gurame', 'Air Tawar')
elang1 = elang('Elang Jawa', 'Ikan', 'Daratan Tinggi', 'Bertelur', 'Paruh', 'Terbang')
elang2 = elang('Elang Emas', 'Kelinci', 'Daratan Rendah', 'Bertelur', 'Paruh', 'Terbang')
ular1 = ular('Anakonda', 'Buaya', 'sungai', 'Bertelur', 'Jeratan Hingga Lemas', 'Tutul Hitam')
ular2 = ular('Weling', 'Katak', 'Hutan/Pertanian', 'Bertelur', 'Menyuntikkan Racun', 'Belang-Belang')

animal1.printAnimal()
ikan1.printJenis()
ikan2.printAir()
elang1.printMulut()
elang2.printCiri()
ular1.printSerang()
ular2.printCorak()