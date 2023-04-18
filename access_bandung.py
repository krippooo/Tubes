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

    

        
