def Biodata(Tahun, Nama, Asal) :
    tahun_sekarang = 2020
    Tahun =  int(Tahun)
    print("Perkenalkan Nama Saya : ",Nama)
    print("Umur Saya :", tahun_sekarang - Tahun)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya Dari :", Asal)
TahunLahir = int(input())
Namaku = input()
Asal = input()
Biodata(TahunLahir,Namaku,Asal)
