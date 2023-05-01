#Fungsi Buatan Tambahan
def cekbahan(bahan_bangunan, bahan):
    """menghitung jumlah bahan yang tersedia"""
    if bahan=="pasir":
        return(int(bahan_bangunan[1][2]))
    if bahan=="batu":
        return(int(bahan_bangunan[2][2]))
    if bahan=="air":
        return(int(bahan_bangunan[3][2]))

def hitungcandi(candi):
    """menghitung banyaknya candi"""
    jumlah_candi=0
    for i in range (110):
        if candi[i][0]!="":
            jumlah_candi+=1
    return(jumlah_candi-1)

#------------------------------------------------
#F06 Bangun
def bangun(uname,users,candi,bahan_bangunan):
    import random
    #Bahan yang dibutuhkan
    batu=random.randint(1,5)
    air=random.randint(1,5)
    pasir=random.randint(1,5)

    #Bahan yang tersedia
    stok_batu=cekbahan(bahan_bangunan,"batu")
    stok_air=cekbahan(bahan_bangunan,"air")
    stok_pasir=cekbahan(bahan_bangunan,"pasir")

    if batu>stok_batu or air>stok_air or pasir>stok_pasir :
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else: #jika bahan ada
        
        #Update Jumlah Bahan Bangunan
        stok_batu-=batu
        stok_air-=air
        stok_pasir-=pasir

        bahan_bangunan[1][2]=str(stok_pasir)
        bahan_bangunan[2][2]=str(stok_batu)
        bahan_bangunan[3][2]=str(stok_air)
        
        jumlah_candi=hitungcandi(candi)
        if jumlah_candi<100: #Bangun dan Simpan Candi
            jumlah_candi+=1

            for i in range (1,110):
                if candi[i][0]=="":
                    candi[i]=[str(i),uname,str(pasir),str(batu),str(air)]
                    break

        sisa_candi= 100-jumlah_candi
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
    return (candi,bahan_bangunan)


#F07 Kumpul
def kumpul(bahan_bangunan):
    #Update Stok Bahan
    if bahan_bangunan[1][0]=="": #jika belum terdefinisi
        bahan_bangunan[1]=["pasir","butiran debu", "0"]
        bahan_bangunan[2]=["batu","butiran besar", "0"]
        bahan_bangunan[3]=["air","tak berbutir", "0"]
        
    #Ambil Bahan
    import random
    batu=random.randint(0,5)
    air=random.randint(0,5)
    pasir=random.randint(0,5)

    #Cek Stok Bahan
    stok_batu=cekbahan(bahan_bangunan,"batu")+batu
    stok_air=cekbahan(bahan_bangunan,"air")+air
    stok_pasir=cekbahan(bahan_bangunan,"pasir")+pasir

    #Update Stok
    bahan_bangunan[1][2]=str(stok_pasir)
    bahan_bangunan[2][2]=str(stok_batu)
    bahan_bangunan[3][2]=str(stok_air)

    #Return
    return(bahan_bangunan)
