#F03 #F04 #F5 #F08 #F09 #F10

#Fungsi Buatan Tambahan
def hitungjin(users):
    """menghitung banyak jin yang ada"""
    jumlah_jin=0
    for i in range(3, 110):
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

        nomor_role=input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        nomor_role=int(nomor_role)
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

#F04
def hapus(users,candi):
    def hitungjini(users):
        jumlah_jin=0
        for i in range(110):
            if users[i][0]!="":
                jumlah_jin+=1
        return jumlah_jin-3
    def usernamejin(arr):
        initjin = [['' for i in range(2)] for j in range(110)]
        for i in range(110):
            if arr[i][2] == "jin_pengumpul" or arr[i][2] == "jin_pembangun":
                initjin[i][0] = arr[i][0]
                initjin[i][1] = arr[i][2]
        username = list(filter(lambda x : x!=['',''], initjin))
        return username
    def isvalid(arr,input):
        cek = False
        i=0
        for i in range(hitungjini(users)):
            if arr[i][0]==input:
                cek = True
        return cek
    userjin = usernamejin(users)
    if userjin != []:
        jin = input("Masukkan username jin : ")
        if isvalid(userjin,jin)==True:
            conf = input(f'apakah anda yakin menghapus jin dengan username {jin} (Y/N)?')
            if conf =="Y" or conf== "y":
                print('Jin telah berhasil dihapus dari alam gaib.')
                count=0
                for i in range(110):
                    hapundi=candi[i]
                    if hapundi[1]==jin:
                        candi[i]=['','','','','']
                        count+=1
                print(f"menghapus total {count} candi.")

                for k in range(110):
                    if users[k][0]==jin:
                        users[k] = ['','','']                
        else:
            print('Tidak ada jin dengan username tersebut.')
    else:
        print("Anda belum memiliki jin, silahkan summon terlebih dahulu.")
    return (users,candi)

#F05 Ubah Jin
def ubahjin (users):
    uname = input("Masukkan username jin :")
    if cekuname (users, uname) == True:
        for i in range (3,110):
            if users[i][0] == uname :
                role = users[i][2]
                break
        if role == "jin_pembangun" :
            change = input("JIn ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)?  ")
            if change == "y" or "Y" :
                role = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
            elif change == "n" or "N":
                print("Jin tidak jadi diubah")
            else :
                print("Silahkan ulangi command, input yang anda berikan salah")
        if role == "jin_pengumpul" :
            change = input("JIn ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?  ")
            if change == "y" or "Y" :
                role = "jin_pembangun"
                print("Jin telah berhasil diubah.")
            elif change == "n" or "N":
                print("Jin tidak jadi diubah")
            else :
                print("Silahkan ulangi command, input yang anda berikan salah")
    if cekuname(users, uname) == False :
        print("Tidak ada jin dengan username tersebut")
    
    for i in range (3,110):
        if users[i][0] == uname :
            users[i][2] = role
            break
        
    return users

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
    def banyakcandi(arr):
        cek = ['','','','','']
        count = 0
        for i in range(1,110):
            if arr[i]!=cek:
                count+=1
        return count
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

            for j in range(total_jin):
                username = jin[j]
                jumlah_candi=banyakcandi(candi)
                if jumlah_candi<100: #Bangun dan Simpan Candi
                    jumlah_candi+=1

                    for i in range (1,110):
                        if candi[i]==['','','','','']:
                            candi[i]=[str(i),username,str(random.randint(1,5)),str(random.randint(1,5)),str(random.randint(1,5))]
                            break

            sisa_candi= 100-jumlah_candi
            print(f"Total {total_jin} candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun, silahkan summon terlebih dahulu')
    return (candi,bahan_bangunan)

#F09 Laporan Jin
def laporanjin(users,candi,bahan_bangunan):
    #Hitung jumlah dan masing-masing tipe jin
    jumlah_jin=0
    jumlah_jin_pengumpul=0
    jumlah_jin_pembangun=0
    for i in range(110):
        if users[i][2]=="jin_pengumpul":
            jumlah_jin+=1
            jumlah_jin_pengumpul+=1
        if users[i][2]=="jin_pembangun":
            jumlah_jin+=1
            jumlah_jin_pembangun+=1

    #Buat list nama jin pembangun dan candi yang ia bangun
    workload_jin_pembangun=[["",0] for i in range(jumlah_jin_pembangun)]
    def cek_di_workload(nama):
        idx=-1
        for i in range(jumlah_jin_pembangun):
            if workload_jin_pembangun[i][0]==nama:
                idx=i
                break
        return idx
    
    for i in range(1,110):
        indeks=cek_di_workload(candi[i][1])
        if indeks!=-1: #sudah tertulis
            workload_jin_pembangun[indeks][1]+=1
        else: #belum tertulis
            for j in range(jumlah_jin_pembangun):
                if workload_jin_pembangun[j][0]=="":
                    workload_jin_pembangun[j][0]=candi[i][1]
                    workload_jin_pembangun[j][1]+=1
                    break

    jin_terajin=workload_jin_pembangun[0][0]
    candi_terajin=workload_jin_pembangun[0][1]
    candi_termalas=workload_jin_pembangun[0][1]
    jin_termalas=workload_jin_pembangun[0][0]
    for i in range(1,jumlah_jin_pembangun):
        if (workload_jin_pembangun[i][1] > candi_terajin):
            jin_terajin=workload_jin_pembangun[i][0]
            candi_terajin=workload_jin_pembangun[i][1]
        elif (workload_jin_pembangun[i][1] == candi_terajin):
            if (workload_jin_pembangun[i][0] < jin_terajin):
                jin_terajin=workload_jin_pembangun[i][0]
                candi_terajin=workload_jin_pembangun[i][1]
        if (workload_jin_pembangun[i][1] < candi_termalas):
            jin_termalas=workload_jin_pembangun[i][0]
            candi_termalas=workload_jin_pembangun[i][1]
        elif (workload_jin_pembangun[i][1] == candi_termalas):
            if (workload_jin_pembangun[i][0] > jin_termalas):
                jin_termalas=workload_jin_pembangun[i][0]
                candi_termalas=workload_jin_pembangun[i][1]

    #Bahan Tersedia
    from access_jin import cekbahan
    stok_batu=cekbahan(bahan_bangunan,"batu")
    stok_air=cekbahan(bahan_bangunan,"air")
    stok_pasir=cekbahan(bahan_bangunan,"pasir")
        
    #Output
    print("============ LAPORAN JIN =============")
    print(f"Total Jin: {jumlah_jin}")
    print(f"Total Jin Pengumpul: {jumlah_jin_pengumpul}")
    print(f"Total Jin Pembangun: {jumlah_jin_pembangun}")
    print(f"Jin Terajin: {jin_terajin} ({candi_terajin})")
    print(f"Jin Termalas: {jin_termalas} ({candi_termalas})")
    print(f"Jumlah Pasir: {stok_pasir} unit")
    print(f"Jumlah Batu: {stok_batu} unit")
    print(f"Jumlah Air: {stok_air} unit")
    

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

    
def batchsummon(users):
    #Melakukan summonjin sekaligus
    n = int(input("Masukkan jin yang ingin Anda summon?"))
    
    for i in range(n):
        jumlah_jin=hitungjin(users)
        if jumlah_jin<100:
            users=summon(users)
    
    return (users)

