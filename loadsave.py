import os
#F13 

#F14 Save
def save(users,candi,bahan_bangunan) :
    
    def saveuser(file_name, users):
        f=open(file_name, "w")
        for user in users:
            f.write(f"{user[0]};{user[1]};{user[2]}\n")


    def savecandi(file_name, candi):
        f=open(file_name, "w")
        for per_candi in candi:
            f.write(f"{per_candi[0]};{per_candi[1]};{per_candi[2]};{per_candi[3]};{per_candi[4]}\n")
            
    def savebahan(file_name, bahan_bangunan):
        f=open(file_name, "w")
        for bahan in bahan_bangunan:
            f.write(f"{bahan[0]};{bahan[1]};{bahan[2]}\n")
            

    direct = os.getcwd()
    ada_save = "save"
    path = os.path.join(direct, ada_save)
    nama_fol = input("Masukan nama folder : ")

    print("\n")
    print("Saving...")

    for files in os.walk(direct):
        if nama_fol not in files :
            os.mkdir(path)
            print("Membuat folder save...")
    for files in os.walk(path):
        if nama_fol in files :
            saveuser('user.csv', users)
            savecandi('candi.csv', candi)
            savebahan('bahan_bangunan.csv', bahan_bangunan)
            print("Berhasil menyimpan data di folder save/"+nama_fol)
        if nama_fol not in files :
            os.mkdir(nama_fol)
            path2 = os.path.join(path,nama_fol)
    for files in os.walk(path2):
        saveuser('user.csv', users)
        savecandi('candi.csv', candi)
        savebahan('bahan_bangunan.csv', bahan_bangunan)
        print("Berhasil menyimpan data di folder save/"+nama_fol)
