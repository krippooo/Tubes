def cekbahan(bahan):
    #read from csv
    #fungsi ini mengembalikan banyaknya bahan (air/pasir/batu)

def hitungcandi():
    #fungsi ini menghitung banyaknya candi yg sudah terbangun
    #read from csv

def bangun():
    #ini prosedur
    #I.S. jin pembangun logged, bahan bangunan stock defined
    #F.S. candi terbangun, sisa  candi/tidak terbangun

    import random
    if akses=="jin_pembangun" : #validasi
        batu=random.randint(1,5)
        air=random.randint(1,5)
        pasir=random.randint(1,5)
        stok_batu=cekbahan("batu")
        stok_air=cekbahan("air")
        stok_pasir=cekbahan("pasir")
        if batu<stok_batu or air<stok_air or pasir<stok_pasir :
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else: #jika bahan ada
            #write to csv
            stok_batu-=batu
            stok_air-=air
            stok_pasir-=pasir
            #cek candi
            candi=hitungcandi()
            if candi<100:
                candi+=1
                #write to csv: [candi, username, pasir, batu, air]
            sisa_candi= 100-candi
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: {sisa candi}")
    else:
        print("Hanya jin pembangun yang dapat membangun candi!")
