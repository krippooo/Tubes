#F03 #F04 #F5 #F08 #F09 #F10

#F03 Summon Jin
def summon():
    kasdf

#F04 Hilangkan Jin
def hapus():
    asddf

#F05 Ubah Jin
def ubah():
    hkj

#F08 Batch Kumpul Bangun
def batchkumpul():
    jkl

def batchbangun():
    adfdaj

#F09 Laporan Jin
def laporanjin():
    adf

#F10 Laporan Candi
def laporancandi(candi):
    #Jumlah Candi
    from access_jin import hitungcandi
    jumlah_candi=hitungcandi(candi)
    
    #Total Bahan
    total_pasir = 0
    for i in range (1, 110):
        if candi[i][2]!="":
            total_pasir+=int(candi[i][2])
    total_batu = 0
    for i in range (1, 110):
        if candi[i][3]!="":
            total_batu+=int(candi[i][3])
    total_air = 0
    for i in range (1, 110):
        if candi[i][4]!="":
            total_pasir+=int(candi[i][4])

    #Harga Candi
    maks=0
    mins=200000
    for i in range(1, 110):
        if candi[i][0]!="":
            harga_candi = 10000 * int(candi[i][2]) + 15000 * int(candi[i][3]) + 7500 * int(candi[i][4])
            if harga_candi>maks:
                maks=harga_candi
                id_termahal= candi[i][0]
            if harga_candi<mins:
                mins=harga_candi
                id_termurah= candi[i][0]

    #Output
    print(f"Total candi: {jumlah_candi}")
    print(f"Total Pasir yang digunakan: {total_pasir}")
    print(f"Total Batu yang digunakan: {total_batu}")
    print(f"Total Air yang digunakan: {total_air}")
    print(f"ID Candi Termahal: {id_termahal} ({maks})")
    print(f"ID Candi Termurah:  {id_termurah} ({mins})")

    

        
