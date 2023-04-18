#F11 #F12

#F11 Hancurkan Candi
def hancurkancandi():
    print("asdf")

#F12 Ayam Berkokok
def ayamberkokok():
    from main import candi
    def panjanglist(arr):
        cek = ['','','','']
        count = 0
        if arr[-1] != cek:
            while arr[count] != cek:
                cek = arr[count]
                count+=1
            return count-2
        else:
            return 100
    f = open('candi.csv','r')
    total = panjanglist(candi)
    if total < 100:
        print("Kukuruyuk.. Kukuruyuk..\n")
        print(f"Jumlah Candi: {total}\n")
        print("Selamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
        exit()
    else:
        print("Kukuruyuk.. Kukuruyuk..\n")
        print(f"Jumlah Candi: {total}\n")
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()




