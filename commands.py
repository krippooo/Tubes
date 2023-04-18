import access_all, access_bandung, access_jin, access_roro, loadcsv

def run(input,role,uname,users,candi,bahan_bangunan):
    #Akses: Semua
    if input=="login":
        if role != "-":
            if role == "bandung_bondowoso" :
                print("Login gagal!")
                print("Anda telah login dengan username Bandung, silahkan lakukan “logout” sebelum melakukan login kembali.")
            elif role == "roro_jonggrang" :
                print("Login gagal!")
                print("Anda telah login dengan username Roro, silahkan lakukan “logout” sebelum melakukan login kembali.")
        else :
            access_all.login()
            role = login()
    if input=="logout":
        if role!="-":
            role,uname = access_all.logout(role,uname)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    if input=="help":
        access_all.help()
    if input=="exit":
        access_all.exit()
    if input=="tempstate":
        access_all.tempstate(role,uname,users,candi,bahan_bangunan)
        return (role,uname,users,candi,bahan_bangunan)


    #Akses: Bandung Bondowoso
    if input=="summonjin" : 
        if role=="bandung_bondowoso":
            users=access_bandung.summon(users)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="hapusjin":
        if role=="bandung_bondowoso":
            access_bandung.hapus()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="ubahjin":
        if role=="bandung_bondowoso":
            access_bandung.ubah()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="batchkumpul":
        if role=="bandung_bondowoso":
            bahan_bangunan=access_bandung.batchkumpul(bahan_bangunan)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="batchbangun":
        if role=="bandung_bondowoso":
           candi,bahan_bangunan=access_bandung.batchbangun(uname,users,bahan_bangunan)
           return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="laporanjin":
        if role=="bandung_bondowoso":
            access_bandung.laporanjin()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="laporancandi":
        if role=="bandung_bondowoso":
            access_bandung.laporancandi(candi)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    
    #Akses: Roro Jonggrang
    if input=="hancurkancandi":
        if role=="roro_jonggrang":
            access_roro.hancurkancandi()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="ayamberkokok":
        if role=="roro_jonggrang":
            access_roro.ayamberkokok()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    #Akses: Jin Pengumpul
    if input=="kumpul":
        if role=="jin_pengumpul":
            bahan_bangunan=access_jin.kumpul(bahan_bangunan)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    #Akses: Jin Pembangun
    if input=="bangun":
        if role=="jin_pembangun":
            candi,bahan_bangunan=access_jin.bangun(uname,users,candi,bahan_bangunan)
            return (role,uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
