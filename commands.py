import access_all, access_bandung, access_jin, access_roro, loadcsv

def run(input,role,uname,users,candi,bahan_bangunan):
    #Akses: Semua
    if input=="login":
        uname,role=access_all.login(uname,users,role)
    elif input=="logout":
        if role!="-":
            role,uname = access_all.logout(role,uname)
        else:
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    elif input=="help":
        access_all.help()
    elif input=="exit":
        access_all.exit()
    elif input=="tempstate":
        access_all.tempstate(role,uname,users,candi,bahan_bangunan)

    #Akses: Bandung Bondowoso
    elif input=="summonjin" : 
        if role=="bandung_bondowoso":
            users=access_bandung.summon(users)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="hapusjin":
        if role=="bandung_bondowoso":
            access_bandung.hapus()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="ubahjin":
        if role=="bandung_bondowoso":
            access_bandung.ubah()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="batchkumpul":
        if role=="bandung_bondowoso":
            bahan_bangunan=access_bandung.batchkumpul(bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="batchbangun":
        if role=="bandung_bondowoso":
           candi,bahan_bangunan=access_bandung.batchbangun(uname,users,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="laporanjin":
        if role=="bandung_bondowoso":
            access_bandung.laporanjin()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="laporancandi":
        if role=="bandung_bondowoso":
            access_bandung.laporancandi(candi)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    
    #Akses: Roro Jonggrang
    elif input=="hancurkancandi":
        if role=="roro_jonggrang":
            access_roro.hancurkancandi()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    elif input=="ayamberkokok":
        if role=="roro_jonggrang":
            access_roro.ayamberkokok()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    #Akses: Jin Pengumpul
    elif input=="kumpul":
        if role=="jin_pengumpul":
            bahan_bangunan=access_jin.kumpul(bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    #Akses: Jin Pembangun
    elif input=="bangun":
        if role=="jin_pembangun":
            candi,bahan_bangunan=access_jin.bangun(uname,users,candi,bahan_bangunan)
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    else:
        print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    return (role,uname,users,candi,bahan_bangunan)
