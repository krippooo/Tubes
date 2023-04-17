import access_all, access_bandung, access_jin, access_roro

def run(input,role):
    #Akses: Semua
    if input=="login":
        access_all.login()
    if input=="logout":
        if role!="":
            access_all.logout()
        else:
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    if input=="help":
        access_all.help()
    if input=="exit":
        access_all.exit()

    #Akses: Bandung Bondowoso
    if input=="summonjin" : 
        if role=="bandung_bondowoso":
            access_bandung.summon()
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
            access_bandung.batchkumpul()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="batchbangun":
        if role=="bandung_bondowoso":
            access_bandung.batchbangun()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="laporanjin":
        if role=="bandung_bondowoso":
            access_bandung.laporanjin()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
    if input=="laporancandi":
        if role=="bandung_bondowoso":
            access_bandung.laporancandi()
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
            access_jin.kumpul()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    #Akses: Jin Pembangun
    if input=="bangun":
        if role=="jin_pembangun":
            access_jin.bangun()
        else:
            print("Anda tidak dapat melakukannya. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")

    else:
        print("Command tersebut tidak ada. Silakan gunakan command 'help' untuk melihat yang dapat Anda lakukan.")
