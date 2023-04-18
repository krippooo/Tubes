#F03 #F04 #F5 #F08 #F09 #F10

#Fungsi Buatan Tambahan
def hitungjin(users):
    """menghitung banyak jin yang ada"""
    jumlah_jin=0
    for i in range(110):
        if users[i][0]!="":
            jumlah_jin+=1
    return jumlah_jin

def cekuname(users, uname):
    """mengecek apa uname sudah terdaftar"""
    existed=False
    for i in range(110):
        if uname==users[i][0]:
            existed=True
            break
    return(existed)

#F03 Summon Jin
def summon(users):
    jumlah_jin=hitungjin(users)
    if jumlah_jin<100:
        #Memilih Tipe Jin
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")

        nomor_role=int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while nomor_role!=1 and nomor_role!=2:
            print(f"Tidak ada jenis jin bernomor “{nomor_role}”!")
            print("\n")
            nomor_role=int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        
        if nomor_role==1:
            print("Memilih jin 'Pengumpul'")
            role="jin_pengumpul"
        if nomor_role==2:
            print("Memilih jin 'Pembangun'")
            role="jin_pembangun"
        
        #Mendaftarkan Jin
        uname=input("Masukkan username jin: ")
        while cekuname(users,uname):
            print(f"Username “{uname}” sudah diambil!")
            print("\n")
            uname=input("Masukkan username jin: ")

        pw=input("Masukkan password jin: ")
        while len(pw)<5 or len(pw)>25:
            print("Password panjangnya harus 5-25 karakter!")
            pw=input("Masukkan password jin: ")
        
        print("\n")
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")

        #Menyimpan Data Jin
        for i in range(3,110):
            if users[i][0]=="":
                users[i]=[uname,pw,role]
                break

        print("\n")
        print(f"Jin {uname} berhasil dipanggil!")
           
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
    #Return
    return (users)


#F04 Hilangkan Jin
def hapus():
    asddf

#F05 Ubah Jin
def ubah():
    hkj

#F08 Batch Kumpul Bangun
def batchkumpul(users,bahan_bangunan):
    # from main import users
    from access_jin import cekbahan
    import random
    def cekjin(arr):  #cek jumlah jin pengumpul
        count=0
        for i in range(110):
            if arr[i][2]=="jin_pengumpul":
                count+=1
        return count
    jin = cekjin(users)
    batu  = 0  # dibedakan dari kumpul biasa
    pasir = 0
    air   = 0
    print(f"Mengerahkan {jin} jin untuk mengumpulkan bahan.")
    
    if bahan_bangunan[1][0]=="": #jika belum terdefinisi
        bahan_bangunan[1]=["pasir","butiran debu", "0"]
        bahan_bangunan[2]=["batu","butiran besar", "0"]
        bahan_bangunan[3]=["air","tak berbutir", "0"]
        
    #Ambil Bahan
    for i in range(jin):
        batu+=random.randint(0,5) # diloop dan ditambahkan sebanyak jlh jin
        air+=random.randint(0,5)
        pasir+=random.randint(0,5)

    #Cek Stok Bahan
    stok_batu=cekbahan(bahan_bangunan,"batu")+batu
    stok_air=cekbahan(bahan_bangunan,"air")+air
    stok_pasir=cekbahan(bahan_bangunan,"pasir")+pasir

    #Update Stok
    bahan_bangunan[1][2]=str(stok_pasir)
    bahan_bangunan[2][2]=str(stok_batu)
    bahan_bangunan[3][2]=str(stok_air)
    print(f"Jin mengumpulkan total {pasir} pasir, {batu} batu, {air} air")
    #Return
    return(bahan_bangunan)

def batchbangun(candi,users,bahan_bangunan):
    from access_jin import cekbahan
    # from main import candi
    import random
    def panjanglist(arr):
        cek = ['','','','','']
        count = 0
        if arr[-1] == cek:
            while arr[count] != cek:
                cek = arr[count]
                count+=1
            return count-2
    def hitungjin(arr):
        count=0
        for i in range(110):
            if arr[i][2]=="jin_pembangun":
                count+=1
        return count
    def cekjin(arr):
        initjin =['' for i in range(110)]
        for i in range(110):
            if arr[i][2]=="jin_pembangun":
                initjin[i]=arr[i][0]
        jin = list(filter(lambda x: x != '', initjin))
        return jin
    def panjang(arr):
        cek = arr[-1]
        count=1
        i=0
        while arr[i] != cek:
            i+=1
            count+=1
        return count
               
    total_jin = hitungjin(users)
    if total_jin!=0:
        jin = cekjin(users)
        #Bahan yang dibutuhkan
        batu,pasir,air = 0,0,0 # hapus
        for i in range(total_jin):
            batu+=random.randint(1,5) #hapus +
            air+=random.randint(1,5)
            pasir+=random.randint(1,5)
        print(f'Mengerahkan {total_jin} jin untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, {air} air.')
        #Bahan yang tersedia
        stok_batu=cekbahan(bahan_bangunan,"batu") # majukan
        stok_air=cekbahan(bahan_bangunan,"air")
        stok_pasir=cekbahan(bahan_bangunan,"pasir")
        def kurangbahan(stok,kebutuhan):
            if stok > kebutuhan:
                return 0
            else:
                return abs(stok-kebutuhan)
        if pasir>stok_pasir or batu>stok_batu or air>stok_air :
            print(f"Bangun gagal, kurang {kurangbahan(stok_pasir,pasir)} pasir, {kurangbahan(stok_batu,batu)} batu, dan {kurangbahan(stok_air,air)} air.")
        
        else: #jika bahan ada
            
            #Update Jumlah Bahan Bangunan
            stok_batu-=batu
            stok_air-=air
            stok_pasir-=pasir

            bahan_bangunan[1][2]=str(stok_pasir)
            bahan_bangunan[2][2]=str(stok_batu)
            bahan_bangunan[3][2]=str(stok_air)

            for j in range(panjang(jin)):
                username = jin[j]
                jumlah_candi=panjanglist(candi)
                if jumlah_candi<100: #Bangun dan Simpan Candi
                    jumlah_candi+=1

                    for i in range (1,110):
                        if candi[i]==['','','','','']:
                            candi[i]=[str(i),username,random.randint(1,5),random.randint(1,5),random.randint(1,5)]
                            break

            sisa_candi= 100-jumlah_candi
            print(f"Total {total_jin} candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun, silahkan summon terlebih dahulu')
    return (candi,bahan_bangunan)

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
            total_air+=int(candi[i][4])

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

    

        
