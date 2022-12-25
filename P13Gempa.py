class Gempa:
  lokasi = ''
  skala = ''

  def __init__(self, tempat, tingkat):
    self.lokasi = tempat
    self.skala = tingkat
  
  def dampak(self):
    if(self.skala < 2):
      print('Laporan Gempa', self.lokasi)
      print('Gempa yang terjadi di', self.lokasi, 'dengan skala', self.skala, 'ricther memiliki dampak gempa tidak terasa.\n')
    elif(self.skala >= 2 and self.skala < 4):
      print('Laporan Gempa', self.lokasi)
      print('Gempa yang terjadi di', self.lokasi, 'dengan skala', self.skala, 'ricther memiliki dampak gempa berupa bangunan retak-retak.\n')
    elif(self.skala >= 4 and self.skala <= 6):
      print('Laporan Gempa', self.lokasi)
      print('Gempa yang terjadi di', self.lokasi, 'dengan skala', self.skala, 'ricther memiliki dampak gempa berupa bangunan runtuh.\n')
    elif(self.skala > 6):
      print('Laporan Gempa', self.lokasi)
      print('Gempa yang terjadi di', self.lokasi, 'dengan skala', self.skala, 'ricther memiliki dampak gempa berupa bangunan runtuh dan berpontensi tsunami.\n')