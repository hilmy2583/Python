from ikan import *
from elang import *
from ular import *
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