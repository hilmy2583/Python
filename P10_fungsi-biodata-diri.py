def biodata(nama, alamat, tanggal, umur, tinggi_badan):
    berat_badan_ideal = str((int(tinggi_badan) - 100)-((int(tinggi_badan)- 100) * 10 / 100))
    print('nama: '+ nama)
    print('alamat: '+ alamat)
    print('tanggal lahir: '+ tanggal)
    print('umur: '+ umur)
    print('tinggi badan: '+ tinggi_badan)
    print('berat badan ideal: '+ berat_badan_ideal)

biodata('Muhammad Hilmy','Bogor','25 Agustus 2003','19','161')