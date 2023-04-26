#F11 #F12
import access_all

#F11 Hancurkan Candi
def hancurkancandi(candi):
    id_candi=input("Masukkan ID Candi: ")
    int_id=int(id_candi)

    candi_found=False
    if candi[int_id][0]==id_candi:
        candi_found=True

    if candi_found:
        hancurkan=input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        if hancurkan=="N":
            print("\n")
            print(f"Candi {id_candi} tidak dihancurkan.")
        elif hancurkan=="Y":
            candi[int_id] = ["" for i in range (5)] #Kosongkan candi
            print("\n")
            print(f"Candi {id_candi} telah berhasil dihancurkan.")
        else:
            print("Anda memasukkan input yang salah. Gagal menghancurkan candi.")
    else:
        print("Tidak ada candi dengan ID tersebut.")
    
    return candi

#F12 Ayam Berkokok
def ayamberkokok():
    from main import candi
    # print(candi)
    def panjanglist(arr):
        cek = ['','','','','']
        count = 0
        if arr[-1] == cek:
            while arr[count] != cek:
                cek = arr[count]
                count+=1
            return count-2
        else:
            return 100
    total = panjanglist(candi)
    if total < 100:
        print("Kukuruyuk.. Kukuruyuk..\n")
        print(f"Jumlah Candi: {total}\n")
        print("Selamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
        exit()
    else:
        print("Kukuruyuk.. Kukuruyuk..\n")
        print(f"Jumlah Candi: {100}\n")
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        access_all.exit("")




