import os
#F13 

#F14 Save
def saveuser(file_name, users):
    with open (file_name, "w", newline= '') as data :
        a = csv.writer(data, delimiter= ",")
        a.writerows(users)

def savecandi(file_name, candi):
    with open (file_name, "w", newline= '') as data :
        a = csv.writer(data, delimiter = ",")
        a.writerows(candi)
            
def savebahan(file_name, bahan_bangunan):
    with open (file_name, "w", newline= '') as data :
        a = csv.writer(data, delimiter= ",")
        a.writerows(bahan_bangunan)

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
