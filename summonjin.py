def cekuname(uname):
    import loadcsv
    arr_user=loadcsv.loaduser()
    existed=False
    for i in range(loadcsv.hitunguser()+1):
        if uname==arr_user[i][0]:
            existed=True
            break
    return(existed)

def summon(akses):
    from loadcsv import hitunguser
    jumlah_jin=hitunguser()
    if akses=="bandung_bondowoso":
        if jumlah_jin<100:
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
            
            uname=input("Masukkan username jin: ")
            while cekuname(uname):
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

            f=open("user.csv",'a')
            f.write(f"{uname};{pw};{role}")
            f.close()

            print("\n")
            print(f"Jin {uname} berhasil dipanggil!")
        else:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Hanya Bandung Bondowoso yang dapat summon jin.")
