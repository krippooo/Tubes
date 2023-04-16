def cekbahan(bahan):
    #read from csv
    #fungsi ini mengembalikan banyaknya bahan (air/pasir/batu)
    f=open("bahan_bangunan.csv", 'r')
    if bahan=="pasir":
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
    if bahan=="batu":
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
    if bahan=="air":
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
        baris=f.readline().rstrip()
    ke=1
    ns=""
    for i in range(len(baris)):
        if(baris[i]==';'):
            ke+=1
        elif(ke==3):
            ns+=baris[i]
    ns=int(ns)
    f.close()
    return(ns)
    

def hitungcandi():
    #fungsi ini menghitung banyaknya candi yg sudah terbangun
    #read from csv
    f=open("candi.csv",'r')
    candi=-1
    baris=f.readline()
    while(baris):
        candi+=1
        baris=f.readline()

    return(candi)


def bangun(akses, uname):
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
        if batu>stok_batu or air>stok_air or pasir>stok_pasir :
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else: #jika bahan ada
            
            #Update bahan_bangunan.csv
            stok_batu-=batu
            stok_air-=air
            stok_pasir-=pasir
            
            f=open("bahan_bangunan.csv", 'w')
            f.write("nama;deskripsi;jumlah\n")
            f.write(f"pasir;yang di pantai;{stok_pasir}\n")
            f.write(f"batu;yang di sungai;{stok_batu}\n")
            f.write(f"air; yang di kolam;{stok_air}")
            f.close()

            #cek candi
            candi=hitungcandi()
            if candi<100:
                candi+=1

                f=open("candi.csv",'a')
                f.write("\n")
                f.write(f"{candi};{uname};{pasir};{batu};{air}")
                f.close()
            sisa_candi= 100-candi
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
    else:
        print("Hanya jin pembangun yang dapat membangun candi!")

def kumpul(akses):
    if akses=="jin_pengumpul":
        import random
        batu=random.randint(0,5)
        air=random.randint(0,5)
        pasir=random.randint(0,5)
        
        stok_batu=cekbahan("batu")
        stok_air=cekbahan("air")
        stok_pasir=cekbahan("pasir")

        #Update bahan_bangunan.csv
        stok_batu+=batu
        stok_air+=air
        stok_pasir+=pasir
        
        f=open("bahan_bangunan.csv", 'w')
        f.write("nama;deskripsi;jumlah\n")
        f.write(f"pasir;yang di pantai;{stok_pasir}\n")
        f.write(f"batu;yang di sungai;{stok_batu}\n")
        f.write(f"air; yang di kolam;{stok_air}\n")
        f.close()

        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan  {air} air.")

    else:
        print("Hanya jin pengumpul yang dapat mengumpulkan bahan bangunan.")
